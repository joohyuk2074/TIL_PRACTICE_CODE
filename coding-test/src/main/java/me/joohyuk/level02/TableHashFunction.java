package me.joohyuk.level02;

import java.util.Arrays;

public class TableHashFunction {
    public int solution(int[][] data, int col, int row_begin, int row_end) {
        int answer = 0;

        Arrays.sort(data, (o1, o2) -> o1[col - 1] != o2[col - 1] ? o1[col - 1] - o2[col - 1] : o2[0] - o1[0]);

        for (int i = row_begin; i < row_end + 1; i++) {
            int currentSum = 0;
            for (int j = 0; j < data[i - 1].length; j++) {
                int num = data[i - 1][j];
                currentSum += (num % i);
            }

            answer ^= currentSum;
        }

        return answer;
    }

    public static void main(String[] args) {
        TableHashFunction tableHashFunction = new TableHashFunction();

        int[][] data = {
            {2, 2, 6},
            {1, 5, 10},
            {4, 2, 9},
            {3, 8, 3}
        };
        int col = 2;
        int rowBegin = 2;
        int rowEnd = 3;


        int solution = tableHashFunction.solution(data, col, rowBegin, rowEnd);
        System.out.println(solution);
    }
}
