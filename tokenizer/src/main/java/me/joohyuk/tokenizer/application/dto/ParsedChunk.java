package me.joohyuk.tokenizer.application.dto;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Getter;
import lombok.ToString;
import me.joohyuk.tokenizer.application.dto.docmeta.DocMetaDto;
import me.joohyuk.tokenizer.application.dto.semanticchunk.SemanticChunkDto;

import java.util.List;

@Getter
@ToString
public class ParsedChunk {

    @JsonProperty("doc_meta")
    private DocMetaDto docMetaDto;

    @JsonProperty("chunks")
    private List<SemanticChunkDto> chunks;

}
