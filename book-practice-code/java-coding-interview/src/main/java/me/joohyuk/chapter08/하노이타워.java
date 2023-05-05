package me.joohyuk.chapter08;

public class 하노이타워 {

    public static void hanoiTower(int n, String from, String tmp, String to) {
        if (n==1) {
            System.out.println("원판 " + 1 + "을 " + from + "에서 " + to + "로 옮긴다.");
        } else {
            hanoiTower(n-1, from, to, tmp);
            System.out.println("원판 " + n + "을 " + from + "에서 " + to + "로 옮긴다.");
            hanoiTower(n-1, tmp, from, to);
        }
    }

    public static void main(String[] args) {
        hanoiTower(3, "a", "b", "c");
    }
}
