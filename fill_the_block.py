"""
Height x Width 의 보드가 검은색과 흰색으로 채워져 있다.

모든 흰칸을 L자 모양의 흰색 블록으로 덮고 싶다.

블록은 회전 가능하지만 겹치거나 검은 색을 침범하거나

밖으로 나가서는 안된다.

보드가 있을 때 이를 덮는 방법의 수를 계산하는 프로그램을 만드세요.
"""

H = 8
W = 10
board = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

cases = [
    [[1, 0], [0, 1], [0, 0]],
    [[0, 1], [1, 1], [0, 0]],
    [[1, 0], [1, 1], [0, 0]],
    [[1, 0], [1, -1], [0, 0]]
]


def in_range(y, x):
    if y < 0 or x < 0 or y <= H or x <= W:
        return True
    return False


def put(y, x, c):
    ret = True
    for point in c:
        _y = y + point[0]
        _x = x + point[1]
        if not in_range(_y, _x):
            ret = False
        else:
            board[_y][_x] += 1
            if board[_y][_x] > 1:
                ret = False
    return ret


def get(y, x, c):
    for point in c:
        _y = y + point[0]
        _x = x + point[1]
        if not in_range(_y, _x):
            continue
        else:
            board[_y][_x] -= 1


def solve():
    first_x = first_y = None
    for i in range(H):
        for j in range(W):
            if board[i][j] == 0:
                first_y = i
                first_x = j
                break
        if first_x != None:
            break

    if first_x == None:
        return 1

    ret = 0

    for c in cases:
        if put(first_y, first_x, c):
            ret += solve()
        get(first_y, first_x, c)

    return ret
