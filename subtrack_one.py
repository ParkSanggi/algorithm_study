# 두 개의 문자열을 최대 한 번만 수정했을 때 같아질 수 있는지 확인하는 함수를 만드세요.

string1 = "aabb"
string2 = "abbb"


def compare_strings(a, b):
    length_a = len(a)
    length_b = len(b)

    # imutable인 문자열을 수정할수도 있다는 생각에 리스트로 변환
    # 메모리 문제, 변경 시 정렬문제 있음
    list_a = list(a)
    list_b = list(b)

    inconsistancy_count = 0

    # 문자열의 길이가 같다면 다른 부분을 찾아서 같게 만들고 일치하는지 확인
    if length_a == length_b:
        for i in range(length_a):
            if list_a[i] == list_b[i]:
                continue
            else:
                list_b[i] = list_a[i]

                if list_a != list_b:
                    return False

    # 문자열 길이의 차이가 1이라면 다른 부분을 찾아 고치거나, 삭제하고 같은지 확인
    elif abs(length_a - length_b) == 1:
        for i in range(length_a - 1):
            if list_a[i] == list_b[i]:
                continue
            else:
                list_b.insert(i, list_a[i])
                print(list_b)

                if list_a != list_b:
                    return False

        if length_a - length_b < 0:
            if length_b[:-1] != length_a:
                return False

    else:
        return False

    return True
