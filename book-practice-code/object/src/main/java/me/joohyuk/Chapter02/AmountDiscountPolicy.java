package me.joohyuk.Chapter02;

public class AmountDiscountPolicy extends DefaultDiscountPolicy {

    private final Money discountAmount;

    public AmountDiscountPolicy(Money discountAmount, DiscountCondition... conditions) {
        super(conditions);
        this.discountAmount = discountAmount;
    }

    @Override
    public Money getDiscountAmount(Screening screening) {
        return this.discountAmount;
    }
}
