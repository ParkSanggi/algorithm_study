from copy import copy

string = ['a', 'b', 'c', 'd']


def find_permutation(_list):
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