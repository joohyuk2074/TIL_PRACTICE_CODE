package me.joohyuk.tokenizer.application.module;

import jakarta.annotation.PostConstruct;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import me.joohyuk.tokenizer.application.dto.gpt.ChatGptMessage;
import me.joohyuk.tokenizer.application.dto.gpt.ChatGptRequest;
import me.joohyuk.tokenizer.application.dto.gpt.ChatGptResponse;
import me.joohyuk.tokenizer.application.dto.gpt.Role;
import org.springframework.beans.factory.annotation.Value;
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
public class AzureOpenAIRequestClient {

    @Value("${azure.gpt.url:https://posicube-demo-dev.openai.azure.com}")
    private String baseUrl;

    @Value("${azure.gpt.api-key:99c24b9213644746ac9ef909ba1bcc15}")
    private String apiKey;

    @Value("${azure.gpt.api-version:2023-03-15-preview}")
    private String apiVersion;

    private WebClient webClient;

    @PostConstruct
    public void setWebClient() {
        Map<String, String> headerMap = new HashMap<>();
        headerMap.put(HttpHeaders.CONTENT_TYPE, MediaType.APPLICATION_JSON_VALUE);
        headerMap.put("api-key", apiKey);

        this.webClient = WebClientFactory.createWebClient(baseUrl, headerMap);
    }

    public String request(String requestText) {
        String uri = "/openai/deployments/gpt-35-turbo-0301/chat/completions?api-version=" + apiVersion;

        ChatGptRequest tableSummaryRequest = getTableSummaryRequest(requestText);

        Mono<ChatGptResponse> response = webClient.post()
            .uri(uri)
            .bodyValue(tableSummaryRequest)
            .retrieve()
            .bodyToMono(ChatGptResponse.class);

        ChatGptResponse chatGptResponse = response.block();
        String content = Objects.requireNonNull(chatGptResponse).getChoices().get(0).getMessage().getContent();
        log.info("Info - table summary text: {}", content);
        return content;
    }

    private ChatGptRequest getTableSummaryRequest(String query) {
        ChatGptMessage systemChatGptMessage = ChatGptMessage.builder()
            .role(Role.SYSTEM.getValue())
            .content("Assistant helps the customers. "
                + "Write sentences that explain the contents of the table provided below. "
                + "Answer ONLY with the facts listed in the table. Keep the original language. "
                + "Table contents are written in HTML format")
            .build();

        ChatGptMessage userChatGptMessage = ChatGptMessage.builder()
            .role(Role.USER.getValue())
            .content(query)
            .build();

        return ChatGptRequest.builder()
            .messages(List.of(systemChatGptMessage, userChatGptMessage))
            .maxTokens(2000)
            .temperature(0.5f)
            .frequencyPenalty(0)
            .presencePenalty(0)
            .stream(false)
            .stop(List.of("<|im_end|>"))
            .build();
    }
}
