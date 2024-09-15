import numpy as np


def eratosthenes(n):
    prime_nums = np.arange(n)
    for i in range(2, int(np.sqrt(n)) + 1):
        if prime_nums[i]:
            for j in range(i * i, n, i):
                prime_nums[j] = 0
    prime_nums[1] = 0
    return prime_nums[prime_nums != 0]


n = 1000
arr = eratosthenes(n)
print(arr)
