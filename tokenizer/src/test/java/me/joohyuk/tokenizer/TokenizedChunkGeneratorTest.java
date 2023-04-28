package me.joohyuk.tokenizer;

import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;
import me.joohyuk.tokenizer.application.dto.semanticchunk.SemanticResultChunkDto;
import me.joohyuk.tokenizer.application.dto.tokenizedchunk.TokenizedChunkDto;
import me.joohyuk.tokenizer.application.generator.TokenizedChunkGenerator;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.springframework.core.io.ClassPathResource;
import org.springframework.core.io.Resource;

import java.io.IOException;
import java.util.List;

public class TokenizedChunkGeneratorTest {

    private TokenizedChunkGenerator tokenizedChunkGenerator;

    private ObjectMapper objectMapper;

    @BeforeEach
    public void init() {
        tokenizedChunkGenerator = new TokenizedChunkGenerator();
        objectMapper = new ObjectMapper();
    }

    @Test
    public void generateToken() throws IOException {
        // given
        Resource resource = new ClassPathResource("result/tokenized/semantic_result_chunk_dto_list.json");
        List<SemanticResultChunkDto> list = objectMapper.readValue(resource.getInputStream(), new TypeReference<>() {
        });

        // when
        List<TokenizedChunkDto> result = tokenizedChunkGenerator.generate(list);

        // then
        for (SemanticResultChunkDto semanticResultChunkDto : list) {
            System.out.println(semanticResultChunkDto.getSemanticChunkUuid());
        }
    }
}