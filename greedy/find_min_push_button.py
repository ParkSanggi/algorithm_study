"""
작성해야 하는 글자 name이 주어진다.

이전 알파벳, 다음 알파벳 버튼으로 알파벳을 변환할 수 있고
커서를 왼쪽, 오른쪽으로 이동할 수 있다.
(a에서 이전을 누르면 z로 가장 왼쪽에서 다시 왼쪽을 누르면 커서가 오른쪽 끝으로 이동)

시작 알파벳이 모두 A일 때 name을 작성하기 위한
최소한의 조작 횟수를 구하는 함수를 구현하세요.
"""

import string


def solution(name):
    # 알파벳을 입력하기 위한 클릭 횟수를 담아 놓는 딕셔너리
    alpha_idx = {}

    subtract_change = -2
    for idx, alpha in enumerate(string.ascii_uppercase):
        # 뒤에서 접근하는게 더 빠른 경우가 있어 14부터는 다시 클릭 횟수를 감소시킴
        if idx > 13:
            alpha_idx[f'{alpha}'] = idx + subtract_change
            subtract_change -= 2
        else:
            alpha_idx[f'{alpha}'] = idx

    temp_name = ['A' for _ in range(len(name))]

    # 해당 자리에 있는 알파벳이 체크되었는지 확인
    match_status = [False for _ in range(len(name))]
    match_count = 0

    move_count = 0
    cur_idx = 0

    # 알파벳을 모두 체크했다면 종료
    while match_count != len(name):

        right_count = 0
        left_count = 0

        if temp_name[cur_idx] != name[cur_idx]:
            temp_name[cur_idx] = name[cur_idx]

            move_count += alpha_idx[name[cur_idx]]

            match_status[cur_idx] = True
            match_count += 1

            if match_count == len(name):
                break

        right_idx = cur_idx

        # 다음으로 이동할 방향을 정하기위해 오른쪽, 왼쪽 모두 다음 변경할 글자의 도달 클릭 수를 체크
        while True:
            right_idx = 0 if right_idx + 1 > len(name) - 1 else right_idx + 1
            right_count += 1

            if temp_name[right_idx] != name[right_idx]:
                break
            else:
                # 이동하면서 변경해야 할 글자가 아니더라도 확인했음을 표시
                if not match_status[right_idx]:
                    match_status[right_idx] = True
                    match_count += 1

        left_idx = cur_idx

        while True:
            left_idx -= 1
            left_count += 1

            if temp_name[left_idx] != name[left_idx]:
                break
            else:
                if not match_status[left_idx]:
                    match_status[left_idx] = True
                    match_count += 1

        # 오른쪽, 왼쪽의 클릭횟수를 비교하여 클릭횟수가 적은 쪽으로 일단 이동(greedy)
        if right_count > left_count:
            cur_idx = left_idx
            move_count += left_count
        else:
            cur_idx = right_idx
            move_count += right_count

    return move_count
