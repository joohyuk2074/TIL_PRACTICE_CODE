package me.joohyuk.tokenizer.application.processor;

import lombok.AccessLevel;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.core.ParameterizedTypeReference;
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
public class TranslateProcessor {

    private final WebClient webClient;

    public String translate(String requestText, String sourceLanguage, String targetLanguage) {
        Map<String, String> uriVariables = new HashMap<>();
        uriVariables.put("api-version", "3.0");
        uriVariables.put("from", sourceLanguage);
        uriVariables.put("to", targetLanguage);

        String uri = "/translate?api-version={api-version}&from={from}&to={to}";
        RequestBody requestBody = RequestBody.from(requestText);

        Mono<List<ResponseBody>> response = webClient.post()
            .uri(uri, uriVariables)
            .bodyValue(List.of(requestBody))
            .retrieve()
            .bodyToMono(new ParameterizedTypeReference<List<ResponseBody>>() {
            });

        List<ResponseBody> responseBodies = response.block();
        ResponseBody responseBody = responseBodies.get(0);

        String translatedText = Objects.requireNonNull(responseBody).getTranslations().get(0).getText();
        log.info("Translate text: {}", translatedText);

        return translatedText;
    }

    @Getter
    @NoArgsConstructor(access = AccessLevel.PRIVATE)
    public static class RequestBody {
        private String text;

        public static RequestBody from(String text) {
            RequestBody requestBody = new RequestBody();
            requestBody.text = text;
            return requestBody;
        }
    }

    @Getter
    @NoArgsConstructor(access = AccessLevel.PRIVATE)
    public static class ResponseBody {
        private List<TranslationItem> translations;

        public List<TranslationItem> getTranslations() {
            return translations;
        }

        public void setTranslations(List<TranslationItem> translations) {
            this.translations = translations;
        }

        @Getter
        @NoArgsConstructor(access = AccessLevel.PRIVATE)
        public static class TranslationItem {
            private String text;

            private String to;
        }
    }
}