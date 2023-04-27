package me.joohyuk.tokenizer.application.dto;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonInclude;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import me.joohyuk.tokenizer.application.dto.passage.PassageDto;

import java.util.UUID;

@Getter
@Builder
@AllArgsConstructor
@NoArgsConstructor
@JsonIgnoreProperties(ignoreUnknown = true)
@JsonInclude(JsonInclude.Include.NON_NULL)
public class TokenizedChunkDto {

    private String tokenizedChunkUuid;

    private String tokenizedChunkId;

    private String semanticChunkUuid;

    private String semanticChunkId;

    private String documentUuid;

    private String title;

    private String heading;

    private String source;

    private String content;

    private TokenizeDto tokenizeDto;

    private SummaryDto summaryDto;

    public void updateSummary(SummaryDto summaryDto) {
        this.summaryDto = summaryDto;
    }

    public PassageDto toPassageDto() {
        String fixedText = "##Title: " + title + "\n##Heading: " + heading + "\n##Content: ";
        String previousSummary = summaryDto.getPreviousSummary();
        String nextSummary = summaryDto.getNextSummary();
        return PassageDto.builder()
            .passageUuid(UUID.randomUUID().toString())
            .documentUuid(this.documentUuid)
            .semanticChunkUuid(this.semanticChunkUuid)
            .semanticChunkId(this.semanticChunkId)
            .tokenizedChunkUuid(this.tokenizedChunkUuid)
            .tokenizedChunkId(this.tokenizedChunkId)
            .title(this.title)
            .heading(this.heading)
            .source(this.source)
            .content(previousSummary + fixedText + content + nextSummary)
            .build();
    }

}
