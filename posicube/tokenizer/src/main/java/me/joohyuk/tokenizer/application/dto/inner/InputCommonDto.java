package me.joohyuk.tokenizer.application.dto.inner;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.AccessLevel;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;

@Getter
@AllArgsConstructor(access = AccessLevel.PRIVATE)
@NoArgsConstructor(access = AccessLevel.PROTECTED)
public class InputCommonDto {

    @JsonProperty("customer_uuid")
    private String customerUUID;

    @JsonProperty("collection")
    private String collection;

    @JsonProperty("source_language")
    private String sourceLanguage;
}
