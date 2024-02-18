from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sums = sum(nums)
        if sums % 2:
            return False

        target = sums // 2
        dp = set([0])

        for i in range(len(nums) - 1, -1, -1):
            tempDp = dp.copy()
            for t in dp:
                tempDp.add(t)
                tempDp.add(t + nums[i])
            dp = tempDp.copy()

        return True if target in dp else False
