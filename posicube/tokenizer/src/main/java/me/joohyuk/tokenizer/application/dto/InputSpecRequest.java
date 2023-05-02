package me.joohyuk.tokenizer.application.dto;

import lombok.*;
import me.joohyuk.tokenizer.application.dto.inner.*;

@Getter
@Builder
@AllArgsConstructor(access = AccessLevel.PRIVATE)
@NoArgsConstructor(access = AccessLevel.PROTECTED)
public class InputSpecRequest {

    private InputCommonDto common;

    private InputParseDto parse;

    private InputTokenizeDto tokenize;

    private InputAthenaDto athena;

    private InputRetrieverDto retriever;

    public void setChunkSavePath(String chunkSavePath) {
        this.parse.setChunkSavePath(chunkSavePath);
    }
}
