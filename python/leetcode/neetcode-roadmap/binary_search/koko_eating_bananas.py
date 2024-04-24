from typing import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right

        while left <= right:
            mid = left + (right - left) // 2
            hoursSpend = 0

            for pile in piles:
                hoursSpend += math.ceil(pile / mid)

            if hoursSpend <= h:
                res = min(res, mid)
                right = mid - 1
            else:
                left = mid + 1

        return res
