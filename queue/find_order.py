from collections import deque


# 인쇄 대기중인 문서의 '우선순위 리스트'와 '확인할 문서'가 주어진다.
# 리스트의 앞에서부터 확인해서 맨 앞 문서의 우선순위보다 높은 순위가 리스트 안에 없을 경우 출력하고,
# 높은 순위가 있을 경우 맨 뒤로 보낼 때 '확인할 문서'의 인쇄 순서를 구하세요.

class Node:
    def __init__(self, n, t):
        self.n = n
        self.t = t


def solution(priorities, location):
    p_list = [Node(p, None) for p in priorities]
    p_list[location].t = True

    waiting = deque()
    waiting.extend(p_list)
    order = 1

    while True:
        bigger_count = 0
        temp = waiting.popleft()

        for p in waiting:
            if p.n > temp.n:
                bigger_count = 1
                break

        if bigger_count == 0:

            if temp.t:
                return order
            else:
                order += 1
        else:
            waiting.append(temp)
