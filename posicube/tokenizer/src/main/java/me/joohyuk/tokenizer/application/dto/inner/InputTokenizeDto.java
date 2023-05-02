package me.joohyuk.tokenizer.application.dto.inner;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.*;

import java.util.List;

@Getter
@Builder
@AllArgsConstructor(access = AccessLevel.PRIVATE)
@NoArgsConstructor(access = AccessLevel.PROTECTED)
public class InputTokenizeDto {

    @JsonProperty("tokenize")
    private List<TokenizeDto> tokenize;

    @Getter
    @Builder
    @AllArgsConstructor(access = AccessLevel.PRIVATE)
    @NoArgsConstructor(access = AccessLevel.PROTECTED)
    public static class TokenizeDto {

        @JsonProperty("target_language")
        private String targetLanguage;

        @JsonProperty("token_size")
        private int tokenSize;

        @JsonProperty("summary_size")
        private int summarySize;

        public SemanticChunk.Tokenize toTokenize() {
            return SemanticChunk.Tokenize.builder()
                .targetLanguage(this.targetLanguage)
                .tokenSize(this.tokenSize)
                .summarySize(this.summarySize)
                .build();
        }
    }

}
