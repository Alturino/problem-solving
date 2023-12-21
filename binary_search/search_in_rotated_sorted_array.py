from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + ((right - left) // 2)

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[mid] < target or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1


s = Solution()
nums = [5, 6, 7, 8, 1, 2, 3, 4]
print(s.search(nums=nums, target=6))
