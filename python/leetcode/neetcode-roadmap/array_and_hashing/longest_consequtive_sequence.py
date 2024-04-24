from typing import List


class Solution:
    # # Time Complexity (N log N)
    # # Space Complexity (1)
    # def longestConsecutive(self, nums: List[int]) -> int:
    #     if len(nums) == 0:
    #         return 0
    #
    #     nums.sort()
    #     longestConsecutive = 0
    #     currentConsecutive = 1
    #     for i in range(len(nums) - 1):
    #         if nums[i] == nums[i + 1]:
    #             continue
    #
    #         if nums[i] + 1 == nums[i + 1]:
    #             currentConsecutive += 1
    #         else:
    #             longestConsecutive = max(longestConsecutive, currentConsecutive)
    #             currentConsecutive = 1
    #     return max(longestConsecutive, currentConsecutive)

    # # Time Complexity (N)
    # # Space Complexity (N)
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for i in numSet:
            if (i - 1) not in numSet:
                length = 1
                while (i + length) in numSet:
                    length += 1
                longest = max(longest, length)
        return longest


# input = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
# input = [9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]
input = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
s = Solution()
print(sorted(input))
print(s.longestConsecutive(input))
