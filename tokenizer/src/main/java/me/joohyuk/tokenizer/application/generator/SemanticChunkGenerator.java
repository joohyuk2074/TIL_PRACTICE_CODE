package me.joohyuk.tokenizer.application.generator;

import com.fasterxml.jackson.databind.ObjectMapper;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import me.joohyuk.tokenizer.application.dto.ContentDto;
import me.joohyuk.tokenizer.application.dto.ParsedChunk;
import me.joohyuk.tokenizer.application.dto.docmeta.DocMetaDto;
import me.joohyuk.tokenizer.application.dto.semanticchunk.SemanticChunkDto;
import me.joohyuk.tokenizer.application.dto.semanticchunk.SemanticResultChunkDto;
import me.joohyuk.tokenizer.application.module.AzureOpenAIRequestClient;
import org.springframework.stereotype.Component;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;

@Slf4j
@RequiredArgsConstructor
@Component
public class SemanticChunkGenerator {

    private final ObjectMapper objectMapper;

    private final AzureOpenAIRequestClient azureOpenAIRequestClient;

    public List<SemanticResultChunkDto> generate(DocMetaDto docMetaDto) {
        String parsedFileFullPath = docMetaDto.getDocumentUri();
        Path jsonFilePath = Paths.get(parsedFileFullPath);
        
        // TODO: 1. 파이썬 플러그인 요청 & uri로 저장된 경로에서 파일 가져오기
        ParsedChunk parsedChunk = getParsedChunk(jsonFilePath);
        // TODO: 2. text타입이 아닌 타입을 모두 text로 변환하기
        List<SemanticChunkDto> chunks = parsedChunk.getChunks();
        for (SemanticChunkDto chunk : chunks) {
             List<SemanticResultChunkDto> semanticResultChunkDtoList = chunk.getContents().stream()
                 .map(semanticChunkDto -> {

                 })
                 .collect(Collectors.toList());
        }

        return Collections.emptyList();
    }

    private ParsedChunk getParsedChunk(Path jsonFilePath) {
        try {
            ParsedChunk parsedChunk = objectMapper.readValue(jsonFilePath.toFile(), ParsedChunk.class);
            log.info("parsedChunk: {}", objectMapper.writerWithDefaultPrettyPrinter().writeValueAsString(parsedChunk));
            return parsedChunk;
        } catch (IOException e) {
            log.error("Failed to parse dto");
            throw new RuntimeException(e);
        }
    }
}
