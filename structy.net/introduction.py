# def max_value(nums):
#     max_val = float('-inf')
#     for n in nums:
#         if n > max_val:
#             max_val = n
#     return max_val

def max_value(nums):
    max_val = float('-inf')
    for n in nums:
        max_val = max(max_val, n)
    return max_val

print(max_value([4, 7, 2, 8, 10, 9]))  # -> 10
print(max_value([-5, -2, -1, -11]))  # -> -1

# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True

from math import sqrt, floor


def is_prime(n):
    if n < 2:
        return False
    # for i in range(2, floor(sqrt(n)) + 1):
    for i in range(2, int(n ** 0.5) + 1):
        if n % 2 == 0:
            return False
    return True


print(is_prime(1))  # -> False
print(is_prime(2))  # -> True
print(is_prime(3))  # -> True
print(is_prime(4))  # -> False
print(is_prime(5))  # -> True
