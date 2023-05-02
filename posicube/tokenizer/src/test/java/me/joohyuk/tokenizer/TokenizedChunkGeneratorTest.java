package me.joohyuk.tokenizer;

import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;
import me.joohyuk.tokenizer.application.dto.docmeta.DocMetaDto;
import me.joohyuk.tokenizer.application.dto.semanticchunk.SemanticResultChunkDto;
import me.joohyuk.tokenizer.application.dto.tokenizedchunk.TokenizedChunkDto;
import me.joohyuk.tokenizer.application.generator.TokenizedChunkGenerator;
import me.joohyuk.tokenizer.application.processor.TranslateProcessor;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.Mock;
import org.springframework.core.io.ClassPathResource;
import org.springframework.core.io.Resource;
import org.springframework.web.reactive.function.client.WebClient;

import java.io.IOException;
import java.util.List;

public class TokenizedChunkGeneratorTest {

    private TokenizedChunkGenerator tokenizedChunkGenerator;

    private ObjectMapper objectMapper;

    @Mock
    private WebClient webClient;

    private TranslateProcessor translateProcessor;

    @BeforeEach
    public void init() {
        translateProcessor = new TranslateProcessor(webClient);
        tokenizedChunkGenerator = new TokenizedChunkGenerator(translateProcessor);
        objectMapper = new ObjectMapper();
    }

    @Test
    public void generateToken() throws IOException {
        // given
        Resource resource = new ClassPathResource("result/tokenized/semantic_result_chunk_dto_list.json");
        List<SemanticResultChunkDto> list = objectMapper.readValue(resource.getInputStream(), new TypeReference<>() {
        });

        // when
        List<TokenizedChunkDto> result = tokenizedChunkGenerator.generate(DocMetaDto.createDefaultDocMetaDto(), list);

        // then
        for (SemanticResultChunkDto semanticResultChunkDto : list) {
            System.out.println(semanticResultChunkDto.getSemanticChunkUuid());
        }
    }
}