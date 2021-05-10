# 백준 7568번 덩치 문제

total_number = int(input())

data_list = []
rank_list = ""

for _ in range(total_number):
    data_list.append(tuple(map(int, input().split())))

for i in range(len(data_list)):
    # 랭크를 확인할 대상을 지정
    target = data_list[i]
    rank_count = 1

    for j in range(len(data_list)):
        # 비교대상이 덩치가 더 크다면 랭크를 뒤로 미룸
        if target[0] < data_list[j][0] and target[1] < data_list[j][1]:
            rank_count += 1
    rank_list = rank_list + f' {rank_count}'

print(rank_list.lstrip())


# 리스트 컴프리헨션을 응용한 숏코딩
l=[list(map(int,input().split()))for i in range(int(input()))]
print(" ".join([str(sum([1for x,y in l if a<x and b<y])+1)for a,b in l]))