def solution(money):
    answer = []
    coins = [50000, 10000, 5000, 1000, 500, 100, 50, 10, 1]
    balance = money

    for coin in coins:
        answer.append(balance // coin)
        balance = balance % coin

    return answer


if __name__ == "__main__":
    money = 543012
    print(money, solution(money))
