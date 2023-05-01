package me.joohyuk.tokenizer.application.dto.semanticchunk;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonInclude;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import me.joohyuk.tokenizer.application.dto.ContentDto;
import me.joohyuk.tokenizer.application.dto.TokenizeDto;
import me.joohyuk.tokenizer.application.dto.tokenizedchunk.TranslatedChunkDto;

import java.util.List;

@Getter
@Builder
@AllArgsConstructor
@NoArgsConstructor
@JsonIgnoreProperties(ignoreUnknown = true)
@JsonInclude(JsonInclude.Include.NON_NULL)
public class SemanticResultChunkDto {

    private String semanticChunkUuid;

    private String semanticChunkId;

    private String documentUuid;

    private String title;

    private String heading;

    private String source;

    private List<ContentDto> contents;

    private List<TokenizeDto> tokenizeDtoList;

    public static SemanticResultChunkDto from(SemanticChunkDto semanticChunkDto){

    }

    public TranslatedChunkDto toTranslatedChunkDto(List<ContentDto> contents, TokenizeDto tokenizeDto) {
        return TranslatedChunkDto.builder()
            .semanticChunkUuid(this.semanticChunkUuid)
            .semanticChunkId(this.semanticChunkId)
            .documentUuid(this.documentUuid)
            .title(this.title)
            .heading(this.heading)
            .source(this.source)
            .contents(contents)
            .tokenizeDto(tokenizeDto)
            .build();
    }

    public TranslatedChunkDto toDefaultTranslatedChunkDto() {
        return TranslatedChunkDto.builder()
            .semanticChunkUuid(this.semanticChunkUuid)
            .semanticChunkId(this.semanticChunkId)
            .documentUuid(this.documentUuid)
            .title(this.title)
            .heading(this.heading)
            .source(this.source)
            .contents(this.contents)
            .build();
    }

}
