package me.joohyuk.tokenizer.application.generator;

import me.joohyuk.tokenizer.application.dto.SemanticChunkDto;
import me.joohyuk.tokenizer.application.dto.TokenizedChunkDto;
import org.springframework.stereotype.Component;

import java.util.List;

@Component
public class TokenizedChunkGenerator {
    Gpt2Tokenizer tokenizer = Gpt2Tokenizer.fromPretrained("gpt2");

    public List<TokenizedChunkDto> generate(List<SemanticChunkDto> chunks) {
        return null;
    }
}
