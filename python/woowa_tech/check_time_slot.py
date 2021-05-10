# 서버 확장을 위해 주어진 로그기록 logs가 찍힌 시간대를 분류하세요.

def solution(logs):
    answer = [0 for i in range(24)]
    logs_list = logs.split("\n")
    for log in logs_list:
        _, time = log.split(" ")
        hour, _, _ = time.split(":")
        hour = int(hour)
        hour += 9
        if hour > 23:
            hour -= 24
        answer[hour] += 1
    return answer