package me.joohyuk.tokenizer.application.dto.inner;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.AccessLevel;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;

@Getter
@AllArgsConstructor(access = AccessLevel.PRIVATE)
@NoArgsConstructor(access = AccessLevel.PROTECTED)
public class InputAthenaDto {
    @JsonProperty("gpt_type")
    private String gptType;

    @JsonProperty("gpt_model_version")
    private String gptModelVersion;

    @JsonProperty("gpt_token_size")
    private String gptTokenSize;

    @JsonProperty("gpt_api_key")
    private String gptApiKey;

    @JsonProperty("athena_api_version")
    private String athenaApiVersion;
}
