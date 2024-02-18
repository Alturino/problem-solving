from typing import List


# [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# [-1, 3, 4, -2, 5, -7]


class Solution:
    # # O(N^3)
    # def maxSubArray(self, nums: List[int]):
    #     maxSum = nums[0]
    #     for i in range(len(nums)):
    #         for j in range(i, len(nums)):
    #             currSum = sum(nums[i:j])
    #             maxSum = max(currSum, maxSum)
    #     return maxSum

    # # O(N^2)
    # def maxSubArray(self, nums: List[int]):
    #     maxSum = nums[0]
    #     for i in range(len(nums)):
    #         currSum = 0
    #         for j in range(i, len(nums)):
    #             currSum += nums[j]
    #             maxSum = max(maxSum, currSum)
    #     return maxSum

    # O(N) Kadane Algorithm
    def maxSubArray(self, arr: List[int]) -> int:
        maxSum = arr[0]
        curSum = 0
        for i in arr:
            if curSum < 0:
                curSum = 0
            curSum += i
            maxSum = max(curSum, maxSum)
        return maxSum

    # # O(N) DP
    # def maxSubArray(self, arr: List[int]) -> int:
    #     maxSum = arr[0]
    #     currMaxSum = arr[0]
    #     for i in range(1, len(arr)):
    #         currMaxSum = max(currMaxSum + arr[i], currMaxSum)
    #         maxSum = max(maxSum, currMaxSum)
    #     return maxSum


s = Solution()
print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
