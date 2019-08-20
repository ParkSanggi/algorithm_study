from copy import copy

# 문자열의 모든 순열을 계산하는 알고리즘을 설계하라
# 모든 문자는 문자열 내에서 고유하게 등장한다고 가정

string = ['a', 'b', 'c', 'd']


def find_permutation(_list):
    # base case
    if len(_list) == 1:
        return [_list]

    last = _list.pop()

    base_elements = find_permutation(_list)

    combined_elements = []

    for element in base_elements:
        for j in range(len(element) + 1):
            base_for_combination = copy(element)
            base_for_combination.insert(j, last)
            combined_elements.append(base_for_combination)
    return base_elements + combined_elements


find_permutation(string)
