# 백준 1009번
# 제곱수의 1의자리 찾기

case_count = int(input())
case_list = [[j for j in map(int, input().split())] for _ in range(case_count)]

for case in case_list:
    temp = [None, int(str(case[0])[-1])]
    square = case[0]

    for i in range(3):
        square *= case[0]
        if i == 2:
            temp[0] = int(str(square)[-1])
        else:
            temp.append(int(str(square)[-1]))
    if temp[case[1] % 4] == 0:
        print(10)
    else:
        print(temp[case[1] % 4])