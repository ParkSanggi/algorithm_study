"""
전체 학생 수 n 과
체육복을 잃어버린 학생 리스트 lost,
여분의 체육복을 가지고 있는 학생 리스트 reserve가 있다.

학생들은 체격순으로 번호가 부여되어 있고 앞과 뒷번호 학생에게만 체육복을 빌려줄 수 있을 때
가장 많은 학생이 수업을 받을 수 있는 경우의 학생 수를 구하세요.

단 여분을 가지고 있는 학생이 잃어버렸을 경우 다른 학생에게 빌려줄 수 없습니다.

프로그래머스 고득점 kit 체육복 문제
"""


def solution(n, lost, reserve):
    lost_count = len(lost)
    reserve_dic = {num: False for num in reserve}
    filtered_lost = lost[:]

    for i in lost:
        if i in reserve_dic:
            del reserve_dic[i]
            filtered_lost.remove(i)
            lost_count -= 1

    for j in filtered_lost:
        if j - 1 in reserve_dic and not reserve_dic[j - 1]:
            reserve_dic[j - 1] = True
            lost_count -= 1

        elif j + 1 in reserve_dic and not reserve_dic[j + 1]:
            reserve_dic[j + 1] = True
            lost_count -= 1

    return n - lost_count
