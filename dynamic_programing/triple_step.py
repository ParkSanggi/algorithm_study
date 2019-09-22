"""
한 번에 계단을 1,2,3계단씩 오를 수 있을 때 n개의 계단을 오르는 방법이 몇가지가 있는지
구하세요.
"""

# def triple_step(n, cur):
#     if n == cur:
#         return 1
#     if n < cur:
#         return 0
#
#     return triple_step(n, cur + 1) + triple_step(n, cur + 2) + triple_step(n, cur + 3)


def triple_step(n, cur, memo):
    if n == cur:
        return 1
    if n < cur:
        return 0

    if cur in memo:
        return memo[cur]
    else:
        memo[cur] = triple_step(n, cur + 1, memo) + triple_step(n, cur + 2, memo) + triple_step(n, cur + 3, memo)
        return memo[cur]


triple_step(100, 0, {})