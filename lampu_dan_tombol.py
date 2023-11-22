import math


def solve(n: int) -> str:
    divCount = 0
    for i in range(1, n + 1):
        if n % i == 0:
            divCount += 1
    return "Lampu Mati" if divCount % 2 == 0 else "Lampu Menyala"


def solve2(n: int) -> str:
    s = round(math.sqrt(n))
    return "Lampu Mati" if s * s != n else "Lampu Menyala"


input = 65
print(solve(input), solve2(input))
