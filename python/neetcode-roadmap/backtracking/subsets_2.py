from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        nums.sort()

        def subsets(start: int):
            if start >= len(nums):
                res.append(subset.copy())
                return

            # Subset that include nums[start]
            subset.append(nums[start])
            subsets(start + 1)
            subset.pop()

            # Subset that don't include nums[start] skip if nums[start] == nums[start + 1]
            # while start + 1 < len(nums) and nums[start] == nums[start + 1]:
            #     start += 1
            for i in range(start + 1, len(nums)):
                if nums[i] == nums[start]:
                    start += 1
            subsets(start + 1)

        subsets(0)
        return res
