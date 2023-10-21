from typing import List


class Solution:
    # The problem with this approach is when we encounter 0 we cannot divise number with 0
    # def productOfArrayExceptSelf(self, nums: List[int]) -> List[int]:
    #     sum = 1
    #     for i in nums:
    #         sum *= i
    #
    #     res = []
    #     for i, v in enumerate(nums):
    #         res[i] = sum // v
    #
    #     return res

    # Time Complexity O(N^2)
    # Space Complexity O(N)
    # def productOfArrayExceptSelf(self, nums: List[int]) -> List[int]:
    #     n = len(nums)
    #     res = [1] * (n)
    #
    #     for i in range(n):
    #         sum = 1
    #         for j in range(n):
    #             if i == j:
    #                 continue
    #
    #             sum *= nums[j]
    #         res[i] = sum
    #
    #     return res

    # Time Complexity O(N)
    # Space Complexity O(1)
    # The result for item in index i is prefix[i - 1] * postfix[i + 1]

    def productOfArrayExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prefix = [1] * (n)
        products = 1
        for i, v in enumerate(nums):
            products *= v
            prefix[i] = products

        postfix = [1] * (n)
        products = 1
        for i in range(n - 1, -1, -1):
            products *= nums[i]
            postfix[i] = products

        res = [1] * (n)
        for i in range(n):
            if i == 0:
                res[i] = 1 * postfix[i + 1]
                i += 1
                continue
            if i == n:
                res[i] = prefix[i - 1] * 1
                break
            res[i] = prefix[i - 1] * postfix[i + 1]
        return res


s = Solution()
print(s.productOfArrayExceptSelf([-1, 1, 0, -3, 3]))
