package me.joohyuk.tokenizer.application.dto.gpt;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

import java.util.List;

@Getter
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class ChatGptRequest {

    private List<ChatGptMessage> messages;

    @JsonProperty("max_tokens")
    private int maxTokens;

    private float temperature;

    @JsonProperty("frequency_penalty")
    private int frequencyPenalty;

    @JsonProperty("presence_penalty")
    private int presencePenalty;

    private boolean stream;

    private List<String> stop;

}
