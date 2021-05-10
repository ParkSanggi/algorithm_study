package algorithm;

import java.util.Arrays;
import java.util.HashMap;

public class Lotto {
    public static void main(String[] args) {
        int[] lottos = {44, 1, 0, 0, 31, 25};
        int[] win_nums = {31, 10, 45, 1, 6, 19};

        System.out.println(Arrays.toString(new Lotto().solution(lottos, win_nums)));
    }

    public int[] solution(int[] lottos, int[] win_nums) {
        int[] rank = {6, 6, 5, 4, 3, 2, 1};
        int eraseCount = 0;
        int winCount = 0;
        HashMap<Integer, Integer> winMap= new HashMap<>();
        int[] answer = new int[2];

        for (int winNum : win_nums) {
            winMap.put(winNum, 1);
        }
        for (int lotto : lottos) {
            if (lotto == 0) {
                eraseCount++;
            }
            winCount += winMap.getOrDefault(lotto, 0);
        }
        answer[0] = rank[winCount + eraseCount];
        answer[1] = rank[winCount];
        return answer;
    }
}
