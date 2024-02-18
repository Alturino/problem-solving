from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMin, curMax = 1, 1

        for n in nums:
            tempMax = curMax * n
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(tempMax, n * curMin, n)
            res = max(res, curMax)
        return res


s = Solution()
print(s.maxProduct([0, 2]))
