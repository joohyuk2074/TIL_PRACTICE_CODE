package me.joohyuk.tokenizer.application.generator;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import me.joohyuk.tokenizer.application.dto.ContentDto;
import me.joohyuk.tokenizer.application.dto.TokenizeDto;
import me.joohyuk.tokenizer.application.dto.docmeta.DocMetaDto;
import me.joohyuk.tokenizer.application.dto.semanticchunk.SemanticResultChunkDto;
import me.joohyuk.tokenizer.application.dto.tokenizedchunk.TokenizedChunkDto;
import me.joohyuk.tokenizer.application.dto.tokenizedchunk.TranslatedChunkDto;
import me.joohyuk.tokenizer.application.processor.TranslateProcessor;
import org.springframework.stereotype.Component;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

@Slf4j
@RequiredArgsConstructor
@Component
public class TokenizedChunkGenerator {
    Gpt2Tokenizer tokenizer = Gpt2Tokenizer.fromPretrained("gpt2");

    private final TranslateProcessor translateProcessor;

    public List<TokenizedChunkDto> generate(DocMetaDto docMetaDto, List<SemanticResultChunkDto> chunks) {
        List<TranslatedChunkDto> translatedChunkDtoList = getTranslatedChunkDtoList(docMetaDto, chunks);

        // TODO: 테스트용
        ObjectMapper objectMapper = new ObjectMapper();
        for (TranslatedChunkDto translatedChunkDto : translatedChunkDtoList) {
            try {
                String result = objectMapper.writerWithDefaultPrettyPrinter().writeValueAsString(translatedChunkDto);
                log.info("TranslatedChunkDto: {}", result);
            } catch (JsonProcessingException e) {
                throw new RuntimeException(e);
            }
        }

        return Collections.emptyList();
    }

    private List<TranslatedChunkDto> getTranslatedChunkDtoList(DocMetaDto docMetaDto, List<SemanticResultChunkDto> chunks) {
        List<TranslatedChunkDto> tokenizedChunkDtoList = new ArrayList<>();

        String sourceLanguage = docMetaDto.getLanguage();
        for (SemanticResultChunkDto semanticChunkDto : chunks) {

            List<TokenizeDto> tokenizeDtoList = semanticChunkDto.getTokenizeDtoList();

            for (TokenizeDto tokenizeDto : tokenizeDtoList) {
                TranslatedChunkDto translatedChunkDto = getTranslatedByLanguage(semanticChunkDto, sourceLanguage, tokenizeDto);
                tokenizedChunkDtoList.add(translatedChunkDto);
            }
        }

        return tokenizedChunkDtoList;
    }

    private TranslatedChunkDto getTranslatedByLanguage(SemanticResultChunkDto semanticChunkDto, String sourceLanguage, TokenizeDto tokenizeDto) {
        if (sourceLanguage.equalsIgnoreCase(tokenizeDto.getTargetLanguage())) {
            return semanticChunkDto.toDefaultTranslatedChunkDto();
        }

        return getTranslatedChunkDto(semanticChunkDto, sourceLanguage, tokenizeDto);
    }

    private TranslatedChunkDto getTranslatedChunkDto(SemanticResultChunkDto semanticChunkDto, String sourceLanguage, TokenizeDto tokenizeDto) {
        String targetLanguage = tokenizeDto.getTargetLanguage();

        String title = semanticChunkDto.getTitle();
        String translatedTitle = translateProcessor.translate(title, sourceLanguage, targetLanguage);

        String heading = semanticChunkDto.getHeading();
        String translatedHeading = translateProcessor.translate(heading, sourceLanguage, targetLanguage);

        List<ContentDto> translatedContents = semanticChunkDto.getContents().stream()
            .peek(contentDto -> {
                String text = contentDto.getText();
                String translateText = translateProcessor.translate(text, sourceLanguage, targetLanguage);
                contentDto.setText(translateText);
            })
            .toList();

        return TranslatedChunkDto.of(semanticChunkDto, translatedTitle, translatedHeading, translatedContents, tokenizeDto);
    }
}
