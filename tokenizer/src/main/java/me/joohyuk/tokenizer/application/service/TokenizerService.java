package me.joohyuk.tokenizer.application.service;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import me.joohyuk.tokenizer.application.dto.ParsedChunk;
import me.joohyuk.tokenizer.application.dto.TokenizedChunkDto;
import me.joohyuk.tokenizer.application.generator.TokenizedChunkGenerator;
import org.springframework.stereotype.Service;

import java.util.List;

@Slf4j
@RequiredArgsConstructor
@Service
public class TokenizerService {

    private final ObjectMapper objectMapper;

    private final TokenizedChunkGenerator tokenizedChunkGenerator;

    public List<TokenizedChunkDto> tokenize(ParsedChunk parsedChunk) {
        try {
            String inputData = objectMapper.writerWithDefaultPrettyPrinter().writeValueAsString(parsedChunk);
            log.info("inputData: {}", inputData);
        } catch (JsonProcessingException e) {
            throw new RuntimeException(e);
        }

        return tokenizedChunkGenerator.generate(parsedChunk.getChunks());
    }
}
