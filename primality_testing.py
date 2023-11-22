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
    # iterationCount = 0

    def isPrimeSqrt(n: int) -> bool:
        stop = round(sqrt(n)) + 1
        # nonlocal iterationCount
        if n <= 1:
            return False
        for i in range(2, stop):
            # iterationCount += 1
            if n % i == 0:
                return False
        return True

    for i in range(2, n + 1):
        # iterationCount += 1
        if isPrimeSqrt(i):
            res.append(i)
    # print("generatePrimeIterative iterationCount:", iterationCount)
    return res


def sieveOfEratosthenes(n: int) -> List[int]:
    notPrime = set()
    res = []
    # iterationCount = 0
    for i in range(2, n + 1):
        # iterationCount += 1
        if i not in notPrime:
            res.append(i)
            j = i * i
            while j <= n:
                # iterationCount += 1
                notPrime.add(j)
                j += i
    # print("sieveOfEratosthenes iterationCount:", iterationCount)
    print("notPrime: ", notPrime)
    return res


input = 10000
a = generatePrimeIterative(input)
b = sieveOfEratosthenes(input)
print(a == b, a, b)
