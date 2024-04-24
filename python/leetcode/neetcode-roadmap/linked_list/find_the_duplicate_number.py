from typing import List


class Solution:
    ## Time Complexity O(Log N)
    ## Space Complexity O(1)
    # def findDuplicate(self, nums: List[int]) -> int:
    #     nums.sort()
    #
    #     i, j = 0, 1
    #     while i < len(nums) and j < len(nums):
    #         if nums[i] == nums[j]:
    #             return nums[i]
    #         i += 1
    #         j += 1
    #     return 0

    # ## Time Complexity O(N)
    # ## Space Complexity O(N)
    # def findDuplicate(self, nums: List[int]) -> int:
    #     s = set()
    #     for i in range(len(nums)):
    #         if nums[i] in s:
    #             return nums[i]
    #         s.add(nums[i])
    #     return 0

    ## Time Complexity O(N)
    ## Space Complexity O(1)
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow


s = Solution()
print(s.findDuplicate(nums=[1, 3, 4, 2, 2]))
