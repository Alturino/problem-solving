from typing import List
import collections


class Solution:
    ## Time Complexity O(K * N) TLE
    ## Space Complexity O(1)
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     if k == 1:
    #         return nums
    #
    #     left, right = 0, 1
    #
    #     res = []
    #     while right < len(nums):
    #         while right - left + 1 < k:
    #             right += 1
    #
    #         subArray = nums[left : right + 1]
    #         latestMax = max(subArray)
    #         res.append(latestMax)
    #         left += 1
    #         right += 1
    #     return res

    # Time Complexity O(N)
    # Space Complexity O(N)
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = collections.deque()  ## Saves index
        left, right = 0, 0

        res = []
        while right < len(nums):
            while dq and nums[dq[-1]] < nums[right]:
                dq.pop()
            dq.append(right)

            if left > dq[0]:
                dq.popleft()

            if right + 1 >= k:
                res.append(nums[dq[0]])
                left += 1
            right += 1

        return res


s = Solution()
print(s.maxSlidingWindow(nums=[8, 7, 6, 9], k=2))
print(s.maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))
print(s.maxSlidingWindow(nums=[1, -1], k=1))
print(s.maxSlidingWindow(nums=[9, 11], k=2))
print(s.maxSlidingWindow(nums=[7, 2, 4], k=2))
