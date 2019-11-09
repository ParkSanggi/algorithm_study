# 주어진 음식들의 prices에 쿠폰 discounts들을 적용하여 
# 최소금액이 나오는 경우의 가격을 리턴하세요.

def solution(prices, discounts):
    answer = 0
    tmp_prices = sorted(prices)
    tmp_discounts = sorted(discounts, reverse=True)
    for discount in tmp_discounts:
        price = tmp_prices.pop()
        price -= price * discount // 100
        answer += price
    for price in tmp_prices:
        answer += price
    return answer