from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        left, right = 0, len(height) - 1
        maxLeft, maxRight = height[left], height[right]

        while left < right:
            if maxLeft < maxRight:
                maxLeft = max(maxLeft, height[left])
                left += 1
            elif 

        return 0
