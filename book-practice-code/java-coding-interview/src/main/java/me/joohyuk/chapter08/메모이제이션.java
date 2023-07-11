package me.joohyuk.chapter08;

public class 메모이제이션 {

    public int fibonacci(int k) {
        return fibonacci(k, new int[k + 1]);
    }

    private int fibonacci(int k, int[] cache) {
        if (k <= 1) {
            return k;
        }

        if (cache[k] > 0) {
            return cache[k];
        }

        cache[k] = fibonacci(k - 2, cache) + fibonacci(k - 1, cache);
        return cache[k];
    }
}
