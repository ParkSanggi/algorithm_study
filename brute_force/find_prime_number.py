from copy import copy


# 숫자로 된 문자열이 주어졌을 때 각 숫자로 만들수 있는 수들 중 소수의 갯수를 구하세요.

def is_prime_number(num):
    if num < 2:
        return False
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True


def find_permutations(_list):
    if len(_list) == 1:
        return [_list]
    last = _list.pop()
    base_elements = find_permutations(_list)
    combined_elements = []
    for element in base_elements:
        for j in range(len(element) + 1):
            base_for_combination = copy(element)
            base_for_combination.insert(j, last)
            combined_elements.append(base_for_combination)
    return base_elements + combined_elements + [[last]]


def solution(numbers):
    prime_count = 0
    all_permutations = find_permutations(list(numbers))
    prime_dic = {}

    for perm in all_permutations:
        result = is_prime_number(int(''.join(perm)))
        digit_perm = int(''.join(perm))
        if result and str(digit_perm) not in prime_dic:
            prime_count += 1
            prime_dic[f"{digit_perm}"] = 1

    return prime_count
