package me.joohyuk.tokenizer.application.processor;

import lombok.AccessLevel;
import lombok.NoArgsConstructor;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Component;
import org.springframework.web.reactive.function.client.WebClient;
import reactor.core.publisher.Mono;

import java.util.HashMap;
import java.util.Map;

@RequiredArgsConstructor
@Component
public class TranslateProcessor {

    private final WebClient webClient;

    public String translate(String requestText, String targetLanguage) {
        Map<String, String> uriVariables = new HashMap<>();
        uriVariables.put("api-version", "3.0");
        uriVariables.put("from", "ko");
        uriVariables.put("to", targetLanguage);

        String uri = "/translate?api-version={api-version}&from={from}&to={to}";

        RequestBody requestBody = RequestBody.from(requestText);

        Mono<String> response = webClient.post()
            .uri(uri, uriVariables)
            .bodyValue(requestBody)
            .retrieve()
            .bodyToMono(String.class);

        String translatedText = response.block();

        System.out.println("Translated text: " + translatedText);

        return translatedText;
    }

    @NoArgsConstructor(access = AccessLevel.PRIVATE)
    public static class RequestBody {
        private String text;

        public static RequestBody from(String text) {
            RequestBody requestBody = new RequestBody();
            requestBody.text = text;
            return requestBody;
        }
    }
}
