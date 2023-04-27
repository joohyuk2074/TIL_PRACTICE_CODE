package me.joohyuk.tokenizer.application.dto;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

@Builder
@Getter
@AllArgsConstructor
@NoArgsConstructor
public class SummaryDto {

    private String summaryUuid;

    private String documentUuid;

    private String tokenizedChunkUuid;

    private String tokenizedChunkId;

    private String previousSummary;

    private String nextSummary;
}
