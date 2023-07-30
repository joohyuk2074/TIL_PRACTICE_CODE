package me.joohyuk.graph;

public class Graph {
    public final static int MAX_VERTICES = 50;

    int n;      // 정점의 개수

    int[][] adjMat = new int[MAX_VERTICES][MAX_VERTICES];

    public void init() {
        for (int i = 0; i < MAX_VERTICES; i++) {
            for (int j = 0; j < MAX_VERTICES; j++) {
                adjMat[i][j] = 0;
            }
        }
    }

    public void insertVertex(int v) {
        if (n + 1 > MAX_VERTICES) {
            throw new IllegalArgumentException("그래프: 정점 개수 초과");
        }

        n += 1;
    }

    public void insert_edge(int start, int end) {
        if (start >= n && end >= n) {
            throw new IllegalArgumentException("그래프: 정점 번호 오류");
        }

        adjMat[start][end] = 1;
        adjMat[end][start] = 1;
    }

    public static void main(String[] args) {

    }
}
