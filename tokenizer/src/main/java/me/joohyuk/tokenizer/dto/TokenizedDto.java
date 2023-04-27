package me.joohyuk.tokenizer.dto;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.*;

@Getter
@Builder
@AllArgsConstructor(access = AccessLevel.PRIVATE)
@NoArgsConstructor(access = AccessLevel.PROTECTED)
public class TokenizedDto {

    @JsonProperty("target_language")
    private String targetLanguage;

    @JsonProperty("token_size")
    private int tokenSize;

    @JsonProperty("summary_size")
    private int summarySize;
}
