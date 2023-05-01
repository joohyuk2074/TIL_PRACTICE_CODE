package me.joohyuk.tokenizer.application.dto.semanticchunk;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Getter;
import lombok.Setter;
import me.joohyuk.tokenizer.application.dto.ContentDto;

import java.util.List;

@Getter
//@Setter
@JsonIgnoreProperties(ignoreUnknown = true)
@JsonInclude(JsonInclude.Include.NON_NULL)
public class SemanticChunkDto {

    private String semanticChunkUuid;

    @JsonProperty("chunk_id")
    private String semanticChunkId;

    private String documentUuid;

    private String title;

    private String heading;

    private String source;

    private List<ContentDto> contents;

    public List<String> getTexts() {
        return this.contents.stream()
            .map(ContentDto::getText)
            .toList();
    }

    public SemanticResultChunkDto toSemanticResultChunkDto() {
        return SemanticResultChunkDto.builder()
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
