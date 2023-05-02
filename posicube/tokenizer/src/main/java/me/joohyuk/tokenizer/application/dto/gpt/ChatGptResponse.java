package me.joohyuk.tokenizer.application.dto.gpt;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Getter;

import java.util.List;

@Getter
public class ChatGptResponse {

    private String id;

    private String object;

    private int created;

    private String model;

    private List<Choice> choices;

    private Usage usage;

    @Getter
    public static class Choice {

        private int index;

        @JsonProperty("finish_reason")
        private String finishReason;

        private ChatGptMessage message;
    }

    @Getter
    public static class Usage {

        @JsonProperty("completion_tokens")
        private int completionTokens;

        @JsonProperty("prompt_tokens")
        private int promptTokens;

        @JsonProperty("total_tokens")
        private int totalTokens;

    }

}
