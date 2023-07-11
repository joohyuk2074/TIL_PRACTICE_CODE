package me.joohyuk.chapter08;

public class 태뷸레이션 {
    private int fibonacci(int k) {
        if (k <= 1) {
            return k;
        }

        int first = 1;
        int second = 0;
        int result = 0;

        for (int i = 1; i < k; i++) {
            result = first + second;
            second = first;
            first = result;
        }

        return result;
    }
}
