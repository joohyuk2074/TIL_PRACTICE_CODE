package me.joohyuk.tokenizer.application.module;

import jakarta.annotation.PostConstruct;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import me.joohyuk.tokenizer.application.dto.cognitive.CognitiveRequestBody;
import me.joohyuk.tokenizer.application.dto.cognitive.CognitiveResponseBody;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.core.ParameterizedTypeReference;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.stereotype.Component;
import org.springframework.web.reactive.function.client.WebClient;
import reactor.core.publisher.Mono;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Objects;

@Slf4j
@RequiredArgsConstructor
@Component
public class CognitiveSearchRequestClient {

    @Value("${azure.translator.url:https://api.cognitive.microsofttranslator.com}")
    private String baseUrl;

    @Value("${azure.translator.sub.key:e4716f4f34a842dbba30dc07d89c9181}")
    private String subKey;

    @Value("${azure.translator.sub.region:eastus}")
    private String region;

    private WebClient webClient;

    @PostConstruct
    public void setWebClient() {
        Map<String, String> headerMap = new HashMap<>();
        headerMap.put(HttpHeaders.CONTENT_TYPE, MediaType.APPLICATION_JSON_VALUE);
        headerMap.put("Ocp-Apim-Subscription-Key", "e4716f4f34a842dbba30dc07d89c9181");
        headerMap.put("Ocp-Apim-Subscription-Region", "eastus");

        this.webClient = WebClientFactory.createWebClient(baseUrl, headerMap);
    }

    public String request(String requestText, String sourceLanguage, String targetLanguage) {
        Map<String, String> uriVariables = new HashMap<>();
        uriVariables.put("api-version", "3.0");
        uriVariables.put("from", sourceLanguage);
        uriVariables.put("to", targetLanguage);

        String uri = "/translate?api-version={api-version}&from={from}&to={to}";
        CognitiveRequestBody requestBody = CognitiveRequestBody.from(requestText);

        Mono<List<CognitiveResponseBody>> response = webClient.post()
            .uri(uri, uriVariables)
            .bodyValue(List.of(requestBody))
            .retrieve()
            .bodyToMono(new ParameterizedTypeReference<>() {
            });

        List<CognitiveResponseBody> responseBodies = response.block();
        CognitiveResponseBody responseBody = responseBodies.get(0);

        String translatedText = Objects.requireNonNull(responseBody).getTranslations().get(0).getText();
        log.info("Translate text: {}", translatedText);

        return translatedText;

    }
}
