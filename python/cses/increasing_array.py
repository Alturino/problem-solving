n = int(input())
nums = list(map(int, input().split(" ")))

total = 0
for i in range(1, len(nums)):
    curr, prev = nums[i], nums[i - 1]

    if curr < prev:
        diff = prev - curr
        total += diff
        nums[i] = prev

print(total)
