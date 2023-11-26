package me.joohyuk;

import me.joohyuk.parser.BankStatementAnalyzer;
import me.joohyuk.parser.parser.BankStatementCSVParser;
import me.joohyuk.parser.parser.BankStatementParser;

import java.io.IOException;

public class MainApplication {
    public static void main(String[] args) throws IOException {
        final BankStatementAnalyzer bankStatementAnalyzer = new BankStatementAnalyzer();
        final BankStatementParser bankStatementParser = new BankStatementCSVParser();

        bankStatementAnalyzer.analyze(args[0], bankStatementParser);
    }
}
