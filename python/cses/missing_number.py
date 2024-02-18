n = int(input())
nums = map(int, input().split(" "))
res = sum(nums)
print(int((n * (n + 1) / 2) - res))
