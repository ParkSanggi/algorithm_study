# 정답 answers와 각 학생의 답안지가 주어질 때
# 가장 점수가 높은 학생구하기.

# programmers 코딩테스트 연습 문제

def solution(answers):
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count_list = [0, 0, 0]

    for i in range(1, len(answers) + 1):
        target = answers[i - 1]

        if target == first[i % len(first) - 1]:
            count_list[0] += 1

        if target == second[i % len(second) - 1]:
            count_list[1] += 1

        if target == third[i % len(third) - 1]:
            count_list[2] += 1

    max_count = max(count_list)

    return [i + 1 for i, x in enumerate(count_list) if x == max_count]
