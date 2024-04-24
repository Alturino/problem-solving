from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        sum = 0
        res = (1 << 32) - 1
        for right in range(len(nums)):
            sum += nums[right]
            while sum >= target:
                sum -= nums[left]
                res = min(res, (right - left) + 1)
                left += 1

        if res == (1 << 32) - 1:
            return 0

        return res


s = Solution()
print(s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
print(s.minSubArrayLen(6, [10, 2, 3]))
print(s.minSubArrayLen(4, [1, 4, 4]))
print(s.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))
print(s.minSubArrayLen(11, [1, 2, 3, 4, 5]))
print()
