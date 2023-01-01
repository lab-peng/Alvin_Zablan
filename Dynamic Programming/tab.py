def fib(n):
    table = [0] * (n + 1)
    table[1] = 1
    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i - 2]
    return table[n]


print(fib(6))  # 8
print(fib(7))  # 13
print(fib(8))  # 21
print(fib(50))  # 12_586_269_025


def grid_traveler(m, n):
    table = [[1] * n for i in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            table[i][j] = table[i - 1][j] + table[i][j - 1]
            # print(table)
    return table[m - 1][n - 1]


print(grid_traveler(1, 1))  # 1
print(grid_traveler(2, 3))  # 3
print(grid_traveler(3, 2))  # 3
print(grid_traveler(3, 3))  # 6
print(grid_traveler(18, 18))  # 2_333_606_220
