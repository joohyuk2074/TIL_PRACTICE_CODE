package me.joohyuk.tokenizer.application.generator;

import lombok.RequiredArgsConstructor;
import me.joohyuk.tokenizer.application.dto.ContentDto;
import me.joohyuk.tokenizer.application.dto.TokenizeDto;
import me.joohyuk.tokenizer.application.dto.semanticchunk.SemanticChunkDto;
import me.joohyuk.tokenizer.application.dto.semanticchunk.SemanticResultChunkDto;
import me.joohyuk.tokenizer.application.dto.tokenizedchunk.TokenizedChunkDto;
import me.joohyuk.tokenizer.application.processor.TranslateProcessor;
import org.springframework.stereotype.Component;

import java.util.Collection;
import java.util.Collections;
import java.util.List;

@RequiredArgsConstructor
@Component
public class TokenizedChunkGenerator {
    Gpt2Tokenizer tokenizer = Gpt2Tokenizer.fromPretrained("gpt2");

    private final TranslateProcessor translateProcessor;

    public List<TokenizedChunkDto> generate(List<SemanticResultChunkDto> chunks) {
        // 1. 번역 하는 작업
        for (SemanticResultChunkDto semanticChunkDto : chunks) {
            List<TokenizeDto> tokenizeDtoList = semanticChunkDto.getTokenizeDtoList();
            for (TokenizeDto tokenizeDto : tokenizeDtoList) {
                String targetLanguage = tokenizeDto.getTargetLanguage();
                int totalTokenNum = tokenizeDto.getTokenSize();
                int summaryTokenNum = tokenizeDto.getSummarySize();

                String title = semanticChunkDto.getTitle();
                String heading = semanticChunkDto.getHeading();
                List<ContentDto> contents = semanticChunkDto.getContents();

                String translatedText = translateProcessor.translate(title, targetLanguage);
            }
        }
        return Collections.emptyList();
    }

    private List<String> getTexts(List<SemanticChunkDto> chunks) {
        return chunks.stream()
            .map(SemanticChunkDto::getTexts)
            .flatMap(Collection::stream)
            .toList();
    }
}
