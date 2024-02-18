from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        currMin = nums[0]

        while left <= right:
            if nums[left] < nums[right]:
                return min(currMin, nums[left])

            mid = left + ((right - left) // 2)
            currMin = min(currMin, nums[mid])

            # if nums[mid] > nums[right]:
            #     left = mid + 1
            # else:
            #     right = mid - 1

            if nums[mid] < nums[left]:
                right = mid - 1
            else:
                left = mid + 1

        return min(currMin, nums[left])
