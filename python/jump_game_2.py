from typing import List


def jump(nums: List[int]) -> int:
    res = 0
    left, right = 0, 0
    while right < len(nums):
        farthest = 0
        for i in range(left, right + 1):
            farthest = max(farthest, i + nums[i])
        left = right + 1
        right = farthest
        res += 1
    return res


print(jump(nums=[1, 2, 3]))
