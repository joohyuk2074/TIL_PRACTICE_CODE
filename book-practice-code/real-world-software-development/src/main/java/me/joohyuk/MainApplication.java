package me.joohyuk;

import me.joohyuk.chapter02.BankStatementAnalyzer;
import me.joohyuk.chapter02.BankStatementCSVParser;
import me.joohyuk.chapter02.BankStatementParser;

import java.io.IOException;

public class MainApplication {
    public static void main(String[] args) throws IOException {
        final BankStatementAnalyzer bankStatementAnalyzer = new BankStatementAnalyzer();
        final BankStatementParser bankStatementParser = new BankStatementCSVParser();

        bankStatementAnalyzer.analyze(args[0], bankStatementParser);
    }
}
