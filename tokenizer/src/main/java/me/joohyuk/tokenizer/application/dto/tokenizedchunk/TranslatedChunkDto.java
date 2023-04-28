package me.joohyuk.tokenizer.application.dto.tokenizedchunk;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonInclude;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import me.joohyuk.tokenizer.application.dto.ContentDto;
import me.joohyuk.tokenizer.application.dto.TokenizeDto;

import java.util.List;
import java.util.UUID;

@Getter
@Builder
@AllArgsConstructor
@NoArgsConstructor
@JsonIgnoreProperties(ignoreUnknown = true)
@JsonInclude(JsonInclude.Include.NON_NULL)
public class TranslatedChunkDto {

    private String semanticChunkUuid;

    private String semanticChunkId;

    private String documentUuid;

    private String title;

    private String heading;

    private String source;

    private List<ContentDto> contents;

    private TokenizeDto tokenizeDto;

    public TokenizedChunkDto toTokenizedChunkDto(int subId, String content) {
        return TokenizedChunkDto.builder()
            .tokenizedChunkUuid(UUID.randomUUID().toString())
            .tokenizedChunkId(this.getSemanticChunkId() + "-" + subId)
            .semanticChunkUuid(this.semanticChunkUuid)
            .semanticChunkId(this.semanticChunkId)
            .documentUuid(this.documentUuid)
            .title(this.title)
            .heading(this.heading)
            .source(this.source)
            .content(content)
            .build();
    }

}
