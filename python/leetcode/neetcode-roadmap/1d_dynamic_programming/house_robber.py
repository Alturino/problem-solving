from typing import List


class Solution:
    # def rob(self, nums: List[int]) -> int:
    #     def rob(i: int) -> int:
    #         if i < 0:
    #             return 0
    #         return max(nums[i] + rob(i - 2), rob(i - 1))
    #
    #     return rob(len(nums) - 1)

    # def rob(self, nums: List[int]) -> int:
    #     m = {}
    #
    #     def rob(i: int) -> int:
    #         if i < 0:
    #             return 0
    #
    #         if i in m:
    #             return m[i]
    #
    #         res = max(rob(i - 2) + nums[i], rob(i - 1))
    #         m[i] = res
    #         return res
    #
    #     return rob(len(nums) - 1)

    # def rob(self, nums: List[int]) -> int:
    #     if len(nums) == 0:
    #         return 0
    #
    #     m = [0] * (len(nums) + 1)
    #     m[0] = 0
    #     m[1] = nums[0]
    #     for i in range(1, len(nums)):
    #         m[i + 1] = max(m[i], m[i - 1] + nums[i])
    #
    #     return m[len(nums)]

    # def rob(self, nums: List[int]) -> int:
    #     rob1, rob2 = 0, 0
    #
    #     for n in nums:
    #         temp = max(rob1 + n, rob2)
    #         rob1 = rob2
    #         rob2 = temp
    #
    #     return rob2


s = Solution()
print(s.rob([1, 2, 3, 1]))
