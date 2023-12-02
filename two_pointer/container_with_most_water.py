from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        left, right = 0, len(height) - 1
        while left < right:
            width = right - left
            area = width * min(height[left], height[right])
            maxArea = max(maxArea, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxArea


s = Solution()
print(s.maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]))
