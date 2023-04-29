package me.joohyuk.chapter06;

import java.time.Duration;
import java.time.LocalDateTime;

public class Event {

    private final String subject;
    private final LocalDateTime from;
    private final Duration duration;

    public Event(String subject, LocalDateTime from, Duration duration) {
        this.subject = subject;
        this.from = from;
        this.duration = duration;
    }

    public boolean isSatisfied(RecurringSchedule schedule) {
        if (from.getDayOfWeek() != schedule.getDayOfWeek() ||
            !from.toLocalTime().equals(schedule.getFrom()) ||
            !duration.equals(schedule.getDuration())) {
            return false;
        }
        return true;
    }
//
//    public void reschedule(RecurringSchedule schedule) {
//        from = LocalDateTime.of(from.toLocalDate().plusDays(daysDistance(schedule)), schedule.getFrom());
//    }
}
