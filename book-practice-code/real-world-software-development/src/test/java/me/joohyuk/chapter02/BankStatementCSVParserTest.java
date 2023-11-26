package me.joohyuk.chapter02;

import me.joohyuk.parser.parser.BankStatementCSVParser;
import me.joohyuk.parser.parser.BankStatementParser;
import me.joohyuk.parser.domain.BankTransaction;
import org.junit.jupiter.api.Test;

import java.time.LocalDate;

import static org.assertj.core.api.Assertions.assertThat;

class BankStatementCSVParserTest {

    private final BankStatementParser statementParser = new BankStatementCSVParser();

    @Test
    void shouldParseOneCorrectLine() {
        // given
        final String line = "30-01-2017,-50,Tesco";

        // when
        final BankTransaction result = statementParser.parseFrom(line);

        // then
        assertThat(result.getDate())
            .isEqualTo(LocalDate.of(2017, 1, 30));
        assertThat(result.getAmount())
            .isEqualTo(-50);
        assertThat(result.getDescription())
            .isEqualTo("Tesco");
    }
}