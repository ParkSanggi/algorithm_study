# 음식점의 좌표 restaurant와 각 배달원들의 위치 riders가 주어졌을 때
# 반경 k안에 위치한 배달원들의 수를 리턴하세요.

import math

def solution(restaurant, riders, k):
    answer = 0
    for rider in riders:
        x = abs(rider[0]) - abs(restaurant[0])
        y = abs(rider[1]) - abs(restaurant[1])
        distance = math.sqrt(x**2 + y**2)
        if distance <= k:
            answer += 1
    return answer