import itertools

import itertools


def solution(clothes):
    clothes_dic = {}

    for cloth in clothes:
        if cloth[1] not in clothes_dic:
            clothes_dic[cloth[1]] = [cloth[0]]
        else:
            clothes_dic[cloth[1]].append(cloth[0])

    length_list = [len(clothes_dic[key]) for key in clothes_dic]

    temp = 1
    for i in length_list:
        temp *= i + 1

    return temp - 1

# def solution(clothes):
#     clothes_dic = {}
#
#     for cloth in clothes:
#         if cloth[1] not in clothes_dic:
#             clothes_dic[cloth[1]] = [cloth[0]]
#         else:
#             clothes_dic[cloth[1]].append(cloth[0])
#
#     len_list = []
#
#     for li in clothes_dic:
#         len_list.append(len(clothes_dic[li]))
#
#     ret = 0
#     temp = 1
#
#     for r in range(1, len(clothes_dic) + 1):
#         if r == 1:
#             for length in len_list:
#                 ret += length
#         else:
#             for combination in list(itertools.combinations(clothes_dic.keys(), r)):
#                 for element in combination:
#                     temp *= len(clothes_dic[element])
#                 ret += temp
#                 temp = 1
#
#     return ret
