package me.joohyuk.tokenizer.presentation.controller;

import lombok.RequiredArgsConstructor;
import me.joohyuk.tokenizer.application.dto.ParsedChunk;
import me.joohyuk.tokenizer.application.dto.TokenizedChunkDto;
import me.joohyuk.tokenizer.application.service.TokenizerService;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RequiredArgsConstructor
@RestController
public class TokenizerController {

    private final TokenizerService tokenizerService;

    @PostMapping("/tokenize")
    public List<TokenizedChunkDto> tokenize(@RequestBody ParsedChunk parsedChunk) {
        return tokenizerService.tokenize(parsedChunk);
    }
}
