package me.joohyuk.tokenizer.application.module;

import org.springframework.web.reactive.function.client.WebClient;

import java.util.Map;

public class WebClientFactory {
    public static WebClient createWebClient(String baseUrl, Map<String, String> headers) {
        WebClient.Builder builder = WebClient.builder().baseUrl(baseUrl);
        headers.forEach(builder::defaultHeader);
        return builder.build();
    }
}
