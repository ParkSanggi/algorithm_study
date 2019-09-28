# 프로그래머스 코딩테스트 2번 복기
# 비숍한테 잡히지 않는 자리의 개수 찾기?
# 문제 공유 불가


def check_diagnal(board, row, column, c_change, r_change):
    if board[column][row] == None:
        return
    else:
        board[column][row] = 0
        check_diagnal(board, row + r_change, column + c_change, c_change, r_change)


def solution(bishops):
    board = [[None for _ in range(10)]]
    for _ in range(8):
        board.append([None] + [1 for _ in range(8)] + [None])
    board.append([None for _ in range(10)])

    alpha = ["A", "B", "C", "D", "E", "F", "G", "H"]

    row_table = {a: n + 1 for n, a in enumerate(alpha)}

    for point in bishops:
        row = row_table[point[0]]
        column = 9 - int(point[1])

        board[column][row] = 0

        check_diagnal(board, row, column, -1, -1)
        check_diagnal(board, row, column, -1, +1)
        check_diagnal(board, row, column, +1, -1)
        check_diagnal(board, row, column, +1, +1)

    ret = 0

    for r in board:
        for n in r:
            if n:
                ret += n

    return ret
