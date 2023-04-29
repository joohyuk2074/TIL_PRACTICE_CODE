package me.joohyuk.tokenizer.application.dto.inner;

import com.fasterxml.jackson.annotation.JsonProperty;
import com.posicube.gptdatabackend.common.reflection.ReflectionUtils;
import lombok.AccessLevel;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;

import java.util.stream.Collectors;

@Getter
@AllArgsConstructor(access = AccessLevel.PRIVATE)
@NoArgsConstructor(access = AccessLevel.PROTECTED)
public class InputParseDto {

    @JsonProperty("document_uuid")
    private String documentUUID;

    @JsonProperty("uri")
    private String uri;

    @JsonProperty("uri_save_path")
    private String uriSavePath;

    @JsonProperty("chunk_parser_id")
    private String chunkParserId;

    @JsonProperty("chunk_parser_version")
    private String chunkParserVersion;

    @JsonProperty("chunk_save_path")
    private String chunkSavePath;

    @JsonProperty("file_page_size")
    private String filePageSize;

    @JsonProperty("file_page_type")
    private String filePageType;

    public void setChunkSavePath(String chunkSavePath) {
        this.chunkSavePath = chunkSavePath;
    }

    public String getParserCommand() {
        return ReflectionUtils.getFields(this.getClass()).entrySet().stream()
                .map(entry -> entry.getKey() + "=" + entry.getValue())
                .collect(Collectors.joining(" "));
    }
}
