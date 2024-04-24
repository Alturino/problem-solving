from typing import List


class Solution:
    # def canJump(self, nums: List[int]) -> bool:
    #     goal = len(nums) - 1
    #     for i in range(len(nums) - 2, -1, -1):
    #         if i + nums[i] >= goal:
    #             goal = i
    #     return goal == 0

    def canJump(self, nums: List[int]) -> bool:
        jumps = 0
        for num in nums:
            if jumps < 0:
                return False
            elif num > jumps:
                jumps = num
            jumps -= 1
        return True
