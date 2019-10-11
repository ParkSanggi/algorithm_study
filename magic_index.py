"""
정렬된 배열 A에서 A[i] = i 인 i를 매직 인덱스라고 할 때
마술 인덱스가 존재한다면 그 값을 찾는 메서드를 작성하세요.
"""


# 리스트 내 중복값이 없는 경우
def find_magic_idx(array, start, end):
    # 바이너리 서치를 활용하면 모든 값을 순회하면서 확인하는 것보다 더 빠른 시간엔 값을 찾을 수 있음
    # 리스트가 정렬되어 있을 경우에 한정
    if end < start:
        return -1

    mid_idx = (start + end) // 2

    if array[mid_idx] == mid_idx:
        return mid_idx

    elif array[mid_idx] > mid_idx:
        return find_magic_idx(array, start, mid_idx - 1)

    else:
        return find_magic_idx(array, mid_idx + 1, end)


# 리스트 내 중복값을 허용할 경우
def find_magic_idx2(array, start, end):
    if end < start:
        return -1

    mid_idx = (start + end) // 2

    # 크거나 작을 경우 모두 양쪽에 매직 인덱스를 가질 수 있다.
    if array[mid_idx] == mid_idx:
        return mid_idx

    # 작을 경우 다음 탐색 범위에서 해당 인덱스의 값보다 큰 인덱스를 제외
    left_index = min(mid_idx - 1, array[mid_idx])
    left = find_magic_idx2(array, start, left_index)
    if left >= 0:
        return left

    # 클 경우 다음 탐색 범위에서 해당 인덱스의 값보다 작은 인덱스를 제외
    right_idx = max(mid_idx + 1, array[mid_idx])
    right = find_magic_idx2(array, right_idx, end)
    return right
