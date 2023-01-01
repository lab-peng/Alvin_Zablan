def fib(n):
    return _fib(n)


def _fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n < 2:
        return n
    memo[n] = _fib(n - 1, memo) + _fib(n - 2, memo)
    return memo[n]


print(fib(6))  # 8
print(fib(7))  # 13
print(fib(8))  # 21
print(fib(35))  # 9_227_465
print(fib(50))  # 12_586_269_025

print()


def tribonacci(n):
    return _tribonacci(n)


def _tribonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n < 2:
        return 0
    if n == 2:
        return 1
    memo[n] = _tribonacci(n - 1, memo) + _tribonacci(n - 2, memo) + _tribonacci(n - 3, memo)
    return memo[n]


print(tribonacci(5))  # -> 4
print(tribonacci(14))  # -> 927
print(tribonacci(20))  # -> 35890
print(tribonacci(37))  # -> 1132436852

print()


def sum_possible(amount, numbers):
    return _sum_possible(amount, numbers)


def _sum_possible(amount, numbers, memo={}):
    if amount in memo:
        return memo[amount]

    if amount < 0:
        return False

    if amount == 0:
        return True

    for num in numbers:
        if _sum_possible(amount - num, numbers, memo):
            memo[amount] = True
            return True

    memo[amount] = False
    return False


print(sum_possible(8, [5, 12, 4]))  # -> True, 4 + 4
print(sum_possible(15, [6, 2, 10, 19]))  # -> False
print(sum_possible(13, [6, 2, 1]))  # -> True ???

print()


def min_change(amount, coins):
    ans = _min_change(amount, coins, {})
    if ans == float('inf'):
        return -1
    else:
        return ans


def _min_change(amount, coins, memo):
    if amount in memo:
        return memo[amount]

    if amount == 0:
        return 0

    if amount < 0:
        return float('inf')

    min_coins = float('inf')
    for coin in coins:
        num_coins = 1 + _min_change(amount - coin, coins, memo)
        min_coins = min(min_coins, num_coins)

    memo[amount] = min_coins
    return min_coins


print(min_change(8, [1, 5, 4, 12]))  # -> 2, because 4+4 is the minimum coins possible
print(min_change(13, [1, 9, 5, 14, 30]))  # -> 5
print(min_change(23, [2, 5, 7]))  # -> 4
