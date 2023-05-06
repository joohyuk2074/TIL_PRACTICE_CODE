package me.joohyuk.chapter08;

import java.util.ArrayDeque;
import java.util.Queue;

public class 요세푸스 {

    public static void oprintJosephus(int n, int k) {
        Queue<Integer> circle = new ArrayDeque<>();

        for (int i = 0; i <= n; i++) {
            circle.add(i);
        }

        while (circle.size() != 1) {
            for (int i = 1; i <= k; i++) {
                int eliminated = circle.poll();
                if (i == k) {
                    System.out.println("Eliminated: " + eliminated);
                    break;
                }
                circle.add(eliminated);
            }
        }

        System.out.println("Using queue! Survivor: " + circle.peek());
    }

    public static void main(String[] args) {
        oprintJosephus(15, 3);
    }
}
