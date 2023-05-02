package me.joohyuk.tokenizer.application.dto;

import jakarta.validation.constraints.NotEmpty;
import lombok.AccessLevel;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;


@Getter
@AllArgsConstructor(access = AccessLevel.PRIVATE)
@NoArgsConstructor(access = AccessLevel.PROTECTED)
public class StatusCommandRequest {

    @NotEmpty
    private String documentUUID;

    @NotEmpty
    private TaskType type;

    @NotEmpty
    private TaskStatus status;

    private Object data;
}
