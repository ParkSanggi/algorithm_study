package algorithm;

import java.util.Arrays;

public class MatrixRotation {
    public static void main(String[] args) {
        int rows = 6;
        int columns = 6;
        int[][] queries = {{2,2,5,4},{3,3,6,6},{5,1,6,3}};

        System.out.println(Arrays.toString(new MatrixRotation().solution(rows, columns, queries)));
    }

    public int[] solution(int rows, int columns, int[][] queries) {
        Matrix matrix = new Matrix(rows, columns);
        int[] answer = new int[queries.length];

        for (int i = 0; i < queries.length; i++) {
            answer[i] = matrix.rotate(queries[i]);
        }
        return answer;
    }
}

class Matrix {
    int[][]matrix;

    public Matrix(int rows, int columns) {
        matrix = new int[rows + 2][columns + 2];
        int num = 1;

        for (int row = 1; row < rows + 1; row++) {
            for (int col = 1; col < columns + 1; col++) {
                matrix[row][col] = num;
                num++;
            }
        }
    }

    public int rotate(int[] query) {
        int first = matrix[query[0]][query[1]];
        int min = first;

        min = rotateLeft(query, min);
        min = rotateDown(query, min);
        min = rotateRight(query, min);
        min = rotateUp(query, min);
        matrix[query[0]][query[1] + 1] = first;
        return min;
    }

    public int rotateLeft(int[] query, int min) {
        int start = query[0];
        int end = query[2];

        while (start < end) {
            matrix[start][query[1]] = matrix[start + 1][query[1]];
            start++;
            min = Math.min(matrix[start][query[1]], min);
        }
        return min;
    }

    public int rotateDown(int[] query, int min) {
        int start = query[1];
        int end = query[3];

        while (start < end) {
            matrix[query[2]][start] = matrix[query[2]][start + 1];
            start++;
            min = Math.min(matrix[query[2]][start], min);
        }
        return min;
    }

    public int rotateRight(int[] query, int min) {
        int start = query[2];
        int end = query[0];

        while (start > end) {
            matrix[start][query[3]] = matrix[start - 1][query[3]];
            start--;
            min = Math.min(matrix[start][query[3]], min);
        }
        return min;
    }

    public int rotateUp(int[] query, int min) {
        int start = query[3];
        int end = query[1];

        while (start > end) {
            matrix[query[0]][start] = matrix[query[0]][start - 1];
            start--;
            min = Math.min(matrix[query[0]][start], min);
        }
        return min;
    }
}
