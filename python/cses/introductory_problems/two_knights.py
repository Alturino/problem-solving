def two_knights(n: int) -> int:
    return (n * n) * (n * n - 1) // 2 - (4 * (n - 2) * (n - 1))


n = int(input())
for i in range(1, n + 1):
    print(two_knights(i))
