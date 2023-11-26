package me.joohyuk.parser.domain;

public interface BankTransactionSummarizer {

    double summarize(double accumulator, BankTransaction bankTransaction);
}
