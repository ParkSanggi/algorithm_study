# 입력의 개수를 알 수 없는 경우
# 파일의 끝을 찾아서 종료시킬 수 있다.

try:
    while True:
        a, b = map(int, input().split())
        print(a + b)
except:
    exit()

#
# import sys
#
# for line in sys.stdin:
#     a, b = map(int, line.split())
#     print(a + b)
