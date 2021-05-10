# 알파벳 소문자로만 이루어진 단어 S가 주어진다.
# 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를,
# 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.

from string import ascii_lowercase

alpha_list = list(ascii_lowercase)

s = input()
ret = []
for alpha in alpha_list:
    try:
        ret.append(str(s.index(alpha)))
    except:
        ret.append(str(-1))

print(" ".join(ret))
# print(*ret) * 를 사용하여 언패킹할 수 있음



# 딕셔너리를 사용해서 해당 문자열을 찾는데 걸리는 시간을 줄이고 싶었는데
# 알파벳이 중복되는 경우에 첫번째로 등장하는 인덱스를 찾을 수 없었음
from string import ascii_lowercase

alpha_list = list(ascii_lowercase)

str_dic = {}
str_dic = {j: i for i, j in enumerate(input()) if j not in str_dic}

ret = []

for alpha in alpha_list:
    if alpha in str_dic:
        ret.append(str(str_dic[alpha]))
    else:
        ret.append(str(-1))

print(*ret)
