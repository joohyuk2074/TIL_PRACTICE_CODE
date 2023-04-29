package me.joohyuk.tokenizer.application.dto;

import com.posicube.gptdatabackend.module.manager.task.enums.TaskStatus;
import com.posicube.gptdatabackend.module.manager.task.enums.TaskType;
import lombok.AccessLevel;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;

import javax.validation.constraints.NotEmpty;

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
