"""
소풍

어떤 학교에서 소풍을 간다. 학생들을 두명씩 짝지어 행동하게 하려한다.

서로 친구인 경우에만 짝을 지어야 한다.

서로 친구인 경우의 쌍이 주어질 때

학생들을 짝지을 수 있는 방법의 수를 구하는 프로그램을 구현하라.

first set

학생 수  :  4

친구 쌍 : (0,1) , (1,2), (2,3), (3,0), (0,2), (1,2)
"""

n = 4
friends = [[False for _ in range(n)] for _ in range(n)]
# 학생 간의 관계를 이중행렬로 표현
friends[0][1] = friends[1][0] = True
friends[1][2] = friends[2][1] = True
friends[2][3] = friends[3][2] = True

friends[3][0] = friends[0][3] = True
friends[0][2] = friends[2][0] = True
friends[1][3] = friends[3][1] = True

has_pair = [False for _ in range(n)]


def solve(has_pair):
    first = None
    for i in range(n):
        if has_pair[i] == False:
            first = i
            break
    if first == None:
        return 1
    ret = 0
    for student in range(first + 1, n):
        if not has_pair[student] and friends[first][student]:
            has_pair[student] = has_pair[first] = True
            ret += solve(has_pair)
            has_pair[student] = has_pair[first] = False
    return ret


solve(has_pair)
