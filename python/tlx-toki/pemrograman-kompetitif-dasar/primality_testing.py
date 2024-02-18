from math import sqrt
from typing import List


def isPrimeNaive(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def generatePrimeIterative(n: int) -> List[int]:
    res = []

    def isPrimeSqrt(n: int) -> bool:
        stop = round(sqrt(n)) + 1
        if n <= 1:
            return False
        for i in range(2, stop):
            if n % i == 0:
                return False
        return True

    for i in range(2, n + 1):
        if isPrimeSqrt(i):
            res.append(i)
    return res


# def sieveOfEratosthenes(n: int) -> List[int]:
#     notPrime = set()
#     res = []
#     for i in range(2, n + 1):
#         if i not in notPrime:
#             res.append(i)
#             j = i * i
#             while j <= n:
#                 notPrime.add(j)
#                 j += i
#     return res


# def sieveOfEratosthenes(n: int) -> List[int]:
#     notPrime = set()
#     res = []
#     for i in range(2, n + 1):
#         if i not in notPrime:
#             res.append(i)
#             j = i * i
#             while j <= n:
#                 notPrime.add(j)
#                 j += i
#     return res


def sieveOfEratosthenes(n: int) -> List[int]:
    notPrime = set()
    res = []
    for i in range(2, n + 1):
        if i not in notPrime:
            res.append(i)
            for j in range(i * i, n + 1, i):
                notPrime.add(j)
    return res


input = 100
a = generatePrimeIterative(input)
b = sieveOfEratosthenes(input)
print(b)
