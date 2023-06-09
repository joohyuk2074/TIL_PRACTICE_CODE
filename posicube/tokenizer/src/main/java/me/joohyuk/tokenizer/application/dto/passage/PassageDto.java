package me.joohyuk.tokenizer.application.dto.passage;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import me.joohyuk.tokenizer.application.dto.TokenizeDto;

@Getter
@Builder
@AllArgsConstructor
@NoArgsConstructor
public class PassageDto {

    private String passageUuid;

    private String documentUuid;

    private String semanticChunkUuid;

    private String semanticChunkId;

    private String tokenizedChunkUuid;

    private String tokenizedChunkId;

    private String title;

    private String heading;

    private String source;

    private String content;

    private TokenizeDto tokenizeDto;
}
