package me.joohyuk.Chapter02;

public class PercentageDiscountPolicy extends DefaultDiscountPolicy {

    private final double percent;

    public PercentageDiscountPolicy(double percent, DiscountCondition... conditions) {
        super(conditions);
        this.percent = percent;
    }

    @Override
    public Money getDiscountAmount(Screening screening) {
        return screening.getMovieFee().times(this.percent);
    }
}
