package me.joohyuk.tokenizer.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.reactive.function.client.WebClient;

@Configuration
public class TokenizerConfig {

    @Bean
    public WebClient webClientBuilder() {
        return WebClient.builder()
            .baseUrl("https://api.cognitive.microsofttranslator.com")
            .defaultHeader("Content-Type", "application/json")
            .defaultHeader("Ocp-Apim-Subscription-Key", "e4716f4f34a842dbba30dc07d89c9181")
            .defaultHeader("Ocp-Apim-Subscription-Region", "eastus")
            .build();
    }
}
