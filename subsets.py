from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def subsets(start:int):
            if start >= len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[start])
            subsets(start + 1)
            subset.pop()
            subsets(start + 1)
        subsets(0)
        return res

s = Solution()
print(s.subsets([1,2,3]))
