package me.joohyuk.Chapter02;

import java.time.DayOfWeek;
import java.time.LocalTime;

public class PeriodCondition implements DiscountCondition {

    private DayOfWeek dayOfWeek;

    private LocalTime startTime;

    private LocalTime endTime;

    public PeriodCondition(DayOfWeek dayOfWeek, LocalTime startTime, LocalTime endTime) {
        this.dayOfWeek = dayOfWeek;
        this.startTime = startTime;
        this.endTime = endTime;
    }

    @Override
    public boolean isSatisfiedBy(Screening screening) {
        return screening.getStartTime().getDayOfWeek().equals(this.dayOfWeek) &&
            this.startTime.isBefore(screening.getStartTime().toLocalTime()) &&
            this.endTime.isAfter(screening.getStartTime().toLocalTime());
    }
}
