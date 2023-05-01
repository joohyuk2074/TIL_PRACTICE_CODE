package me.joohyuk.tokenizer.application.dto.cognitive;

import lombok.AccessLevel;
import lombok.Getter;
import lombok.NoArgsConstructor;

@Getter
@NoArgsConstructor(access = AccessLevel.PRIVATE)
public class CognitiveRequestBody {
    private String text;

    public static CognitiveRequestBody from(String text) {
        CognitiveRequestBody requestBody = new CognitiveRequestBody();
        requestBody.text = text;
        return requestBody;
    }

}
