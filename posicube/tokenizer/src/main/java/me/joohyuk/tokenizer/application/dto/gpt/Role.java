package me.joohyuk.tokenizer.application.dto.gpt;

import lombok.AllArgsConstructor;
import lombok.Getter;

@Getter
@AllArgsConstructor
public enum Role {

    SYSTEM("system"),
    USER("user");

    private final String value;

}
