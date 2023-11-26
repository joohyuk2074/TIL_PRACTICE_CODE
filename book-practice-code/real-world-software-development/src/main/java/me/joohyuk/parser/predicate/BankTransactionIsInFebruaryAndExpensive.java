package me.joohyuk.parser.predicate;

import me.joohyuk.parser.domain.BankTransaction;

import java.time.Month;
import java.util.function.Predicate;

public class BankTransactionIsInFebruaryAndExpensive implements Predicate<BankTransaction> {

    @Override
    public boolean test(BankTransaction bankTransaction) {
        return bankTransaction.getDate().getMonth() == Month.FEBRUARY
            && bankTransaction.getAmount() >= 1_000;
    }
}
