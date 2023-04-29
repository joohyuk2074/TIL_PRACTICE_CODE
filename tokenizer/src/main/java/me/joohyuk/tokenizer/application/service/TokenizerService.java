package me.joohyuk.tokenizer.application.service;

import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import me.joohyuk.tokenizer.application.dto.InputSpecRequest;
import me.joohyuk.tokenizer.application.dto.ParsedChunk;
import me.joohyuk.tokenizer.application.dto.docmeta.DocMetaDto;
import me.joohyuk.tokenizer.application.dto.semanticchunk.SemanticResultChunkDto;
import me.joohyuk.tokenizer.application.dto.tokenizedchunk.TokenizedChunkDto;
import me.joohyuk.tokenizer.application.generator.SemanticChunkGenerator;
import me.joohyuk.tokenizer.application.generator.TokenizedChunkGenerator;
import org.springframework.core.io.ClassPathResource;
import org.springframework.stereotype.Service;

import java.io.IOException;
import java.util.Collections;
import java.util.List;
import java.util.UUID;

@Slf4j
@RequiredArgsConstructor
@Service
public class TokenizerService {

    private final ObjectMapper objectMapper;

    private final SemanticChunkGenerator semanticChunkGenerator;

    private final TokenizedChunkGenerator tokenizedChunkGenerator;

    public List<TokenizedChunkDto> tokenize(InputSpecRequest inputSpecRequest) {
        String documentUUID = UUID.randomUUID().toString();
        List<SemanticResultChunkDto> semanticResultChunkDtoList = semanticChunkGenerator.generate(DocMetaDto.createDefaultDocMetaDto());
//        List<TokenizedChunkDto> tokenizedChunkDto = tokenizedChunkGenerator.generate(DocMetaDto.createDefaultDocMetaDto(), chunks);

        ClassPathResource resource = new ClassPathResource("result/tokenized/semantic_result_chunk_dto_list.json");
        try {
            List<SemanticResultChunkDto> chunks = objectMapper.readValue(resource.getInputStream(), new TypeReference<>() {
            });
            tokenizedChunkGenerator.generate(DocMetaDto.createDefaultDocMetaDto(), chunks);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

//        return tokenizedChunkGenerator.generate();
        return Collections.emptyList();
    }
}
