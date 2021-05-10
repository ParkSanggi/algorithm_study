# 서로 다른 값을 가진 배열에서 차이가 k인 쌍의 개수 구하기

s = [1, 7, 5, 9, 2, 12, 3]
k = 2

ret = []

repeat_count = len(s)

for i in range(repeat_count - 1):
    for j in range(i + 1, repeat_count):
        if abs(s[i] - s[j]) == 2:
            ret.append((s[i], s[j]))

# 두번째 원소를 여러번 찾게되서 비효율적 O(NlogN)


dic = {s[i]: i for i in range(len(s))}

confirmed = {}

for i in s:

    if i - k in dic and (i - k, i) not in confirmed:
        confirmed[(i, i - k)] = 1

    if i + k in dic and (i + k, i) not in confirmed:
        confirmed[(i, i + k)] = 1

# 딕셔너리의 키 값 인덱싱을 사용해서 O(N)으로 만들 수 있음
