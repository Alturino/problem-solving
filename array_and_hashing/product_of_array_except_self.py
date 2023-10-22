from typing import List


class Solution:
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     res = [1] * len(nums)
    #     left = 1
    #     right = 1
    #
    #     for i in range(len(nums)):
    #         res[i] = left
    #         left *= nums[i]
    #
    #     for i in range(len(nums) - 1, 0, -1):
    #         res[i] *= right
    #         right *= nums[i]
    #
    #     return res

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * (n)

        for i in range(1, n):
            res[i] = res[i - 1] * nums[i - 1]

        postfix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res


s = Solution()
print(s.productExceptSelf([1, 2, 3, 4]))
