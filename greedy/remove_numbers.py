"""
number가 주어졌을 때 k개의 숫자를 제거하고 만들 수 있는 가장 큰 수 찾기.
"""
from collections import Counter


# 남은 수들로 만들 수 있는 가장 큰 수
from collections import Counter


def solution(number, k):
    answer = ''
    _dict = Counter(number)
    keys = sorted(_dict.keys(), reverse=True)

    min_count = 0
    last = -1

    while min_count < k:
        if _dict[keys[last]] + min_count >= k:
            _dict[keys[last]] -= k - min_count
            min_count += k - min_count
        else:
            min_count += _dict[keys[last]]
            _dict[keys[last]] = 0
            last -= 1

    result = []
    for key in keys:
        for i in range(int(_dict[key])):
            result.append(key)

    answer = "".join(result)

    return answer
