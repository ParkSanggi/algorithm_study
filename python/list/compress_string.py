# 문자열 압축

"""
aabccccaaa 를 a2b1c5a3으로 압축하는 메서드를 작성하세요.
(a 와 A는 구별된다.)
"""

string = 'aabcccaaadd'

count = 1
result = []

for i in range(len(string) - 1):
    if string[i] == string[i + 1]:
        count += 1
    else:
        # 문자열을 뒤에 바로바로 붙여넣는 경우
        # 불필요하게 문자열을 지우고 새로 만드는 과정을 반복해므로 리스트를 이용.
        result.append(string[i])
        result.append(str(count))
        count = 1

result.append(string[-1])
result.append(str(count))

print(''.join(result))
