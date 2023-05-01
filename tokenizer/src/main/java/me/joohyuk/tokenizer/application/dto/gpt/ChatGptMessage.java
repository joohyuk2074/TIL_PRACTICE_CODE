package me.joohyuk.tokenizer.application.dto.gpt;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

@Getter
@Builder
@AllArgsConstructor
@NoArgsConstructor
public class ChatGptMessage {

    private String role;

    private String content;

}