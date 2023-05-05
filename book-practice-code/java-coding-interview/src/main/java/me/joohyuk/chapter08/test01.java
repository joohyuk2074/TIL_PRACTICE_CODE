package me.joohyuk.chapter08;

import java.util.Set;

public class test01 {

    public static class Point {
        int m;
        int n;

        public Point(int m, int n) {
            this.m = m;
            this.n = n;
        }
    }

    public static boolean computePath(int m, int n, boolean[][] maze, Set<Point> path) {

        if (m < 0 || n < 0) {
            return false;
        }

        if (maze[m][n]) {
            return false;
        }

        if (((m == 0) && (n == 0) || computePath(m, n - 1, maze, path) || computePath(m - 1, n, maze, path))) {
            path.add(new Point(m, n));
            return true;
        }

        return false;
    }

    public static void main(String[] args) {

    }
}
