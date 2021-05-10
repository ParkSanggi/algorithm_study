# 두 개의 문자열을 최대 한 번만 수정했을 때 같아질 수 있는지 확인하는 함수를 만드세요.

string1 = "aabb"
string2 = "abbb"


def compare_strings(a, b):
    length_a = len(a)
    length_b = len(b)

    inconsistancy_count = 0

    # 두 문자열의 길이가 같을 경우 각 자리에 있는 문자를 비교하면서 수정횟수가 1을 초과하는지 확인
    if length_a == length_b:
        for i in range(length_a):
            if a[i] == b[i]:
                continue
            else:
                inconsistancy_count += 1
                if inconsistancy_count > 1:
                    return False

    # 문자열 길이의 차이가 1이라면 다른 부분을 찾아 고치거나, 삭제하고 같은지 확인
    elif abs(length_a - length_b) == 1:
        index_a = 0
        index_b = 0

        # 짧은 문자열과 긴 문자열을 항상 같은 위치에서 비교할 수 있게 구분
        if length_a > length_b:
            a, b = b, a
            length_a, length_b = length_b, length_a

        while index_a < length_a and index_b < length_b:
            # 각 문자가 같다면 둘 다 인덱스를 이동시킴
            if a[index_a] == b[index_b]:
                index_a += 1
                index_b += 1
            # 같지 않다면 불일치 카운터를 올리고 긴 문자열의 인덱스만 이동시킴
            else:
                inconsistancy_count += 1
                if inconsistancy_count > 1:
                    return False
                index_b += 1

    else:
        return False

    return True


# 두가지 경우에서 중복되는 부분을 합쳐 한번에 계산하는 방식
def one_edit_away(first, second):
    # 길이 체크
    if abs(len(first) - len(second)) > 1:
        return False

    # 길이가 다른 문자열 구분
    if len(first) > len(second):
        first, second = second, first

    index_first = 0
    index_second = 0

    found_difference = False

    while index_second < len(second) and index_first < len(first):
        if first[index_first] != second[index_second]:
            if found_difference:
                return False
            found_difference = True

            if len(first) == len(second):
                index_first += 1
        else:
            index_first += 1

        index_second += 1

    return True
