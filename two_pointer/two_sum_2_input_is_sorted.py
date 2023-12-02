from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            curSum = numbers[left] + numbers[right]

            if curSum < target:
                left += 1
            elif curSum > target:
                right -= 1
            else:
                return [left + 1, right + 1]

        return []


s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))  # output : [1,2]
print(s.twoSum([2, 3, 4], 6))  # output: [1, 3]
print(s.twoSum([-1, 0], -1))  # output: [1, 2]
