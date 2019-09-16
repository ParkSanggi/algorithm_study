# 행렬을 90도로 회전시키세요.

"""
위쪽 모서리를 오른쪽으로로
오른쪽을 아래쪽으로
아래쪽을 왼쪽으로
왼쪽을 위쪽으로 옮기는 방식으로 회전을 구현하면 된다.

새로운 행렬을 만들어서 구현할 경우 O(n)만큼의 메모리가 추가로 들게되므로
인덱스별로 교체를 진행한다.
"""

matrix = [[]]


def rotate(matrix):
    n = len(matrix)

    layer = 0
    while layer < n / 2:
        first = layer
        last = n - 1 - layer

        i = first
        while i < first:
            offset = i - first
            top = matrix[first][i]

            matrix[first][i] = matrix[last - offset][first]
            matrix[last - offset][first] = matrix[last][last - offset]
            matrix[last][last - offset] = matrix[i][last]
            matrix[i][last] = top
            i += 1

        layer += 1

    return
