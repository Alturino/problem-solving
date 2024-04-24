from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        nums.sort()

        def subsets(start: int = 0):
            if start >= len(nums):
                res.append(subset.copy())
                return

            # Subset that include nums[start]
            subset.append(nums[start])
            subsets(start + 1)
            subset.pop()

            # Subset that don't include nums[start] skip if nums[start] == nums[start + 1]
            while start + 1 < len(nums) and nums[start] == nums[start + 1]:
                start += 1
            subsets(start + 1)

        subsets()
        return res

    # def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    #     res = []
    #     subset = []
    #     nums.sort()
    #
    #     def backtracking(start: int = 0):
    #         res.append(subset.copy())
    #
    #         for i in range(start, len(nums)):
    #             if i > start and nums[i] == nums[i - 1]:
    #                 continue
    #             subset.append(nums[i])
    #             backtracking(i + 1)
    #             subset.pop()
    #
    #     backtracking()
    #     return res
