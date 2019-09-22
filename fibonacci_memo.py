def fibonacci(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    return fibonacci(num - 1) + fibonacci(num - 2)


# memoization

def fibonacci_m(num, memo):
    if num == 0 or num == 1:
        return num
    if num not in memo:
        memo[num] = fibonacci_m(num - 1, memo) + fibonacci_m(num - 2, memo)

    return memo[num]
