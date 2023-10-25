from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        one, two = 0, 0

        for i in nums:
            temp = max(i + one, two)
            one = two
            two = temp

        return two
s = Solution()
print(s.rob([1,2,3,1]))
