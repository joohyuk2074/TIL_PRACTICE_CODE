package me.joohyuk.tokenizer.application.dto.cognitive;

import lombok.AccessLevel;
import lombok.Getter;
import lombok.NoArgsConstructor;

import java.util.List;

@Getter
@NoArgsConstructor(access = AccessLevel.PRIVATE)
public class CognitiveResponseBody {
    private List<CognitiveResponseBody.TranslationItem> translations;

    public List<CognitiveResponseBody.TranslationItem> getTranslations() {
        return translations;
    }

    public void setTranslations(List<CognitiveResponseBody.TranslationItem> translations) {
        this.translations = translations;
    }

    @Getter
    @NoArgsConstructor(access = AccessLevel.PRIVATE)
    public static class TranslationItem {
        private String text;

        private String to;
    }
}
