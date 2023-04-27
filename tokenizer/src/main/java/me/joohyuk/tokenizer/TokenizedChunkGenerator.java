package me.joohyuk.tokenizer;

import me.joohyuk.tokenizer.dto.TokenizedChunkDto;
import me.joohyuk.tokenizer.dto.TranslatedChunkDto;

import java.util.List;

public class TokenizedChunkGenerator {

    Gpt2Tokenizer tokenizer = Gpt2Tokenizer.fromPretrained("gpt2");

    public List<TokenizedChunkDto> chunk(TranslatedChunkDto translatedChunkDto) {

    }
}
