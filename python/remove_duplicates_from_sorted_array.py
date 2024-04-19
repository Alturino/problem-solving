from typing import List


def removeDuplicates(nums: List[int]) -> int:
    left, right = 0, 1
    while right < len(nums):
        if nums[left] != nums[right]:
            left = right
        while (right - left) + 1 > 2:
            nums.pop(right - 1)
            right -= 1
        right += 1
    return len(nums)


# print(removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))
print(removeDuplicates([1, 1, 1]))
