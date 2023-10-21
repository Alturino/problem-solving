from typing import List
class Solution:
    def minCostClimbingStairs(self, costs: List[int]) -> int:
        def minCostClimbingStairs(costs: List[int], curr: int) -> int: 
            if curr == len(costs)+ 1:
                return curr
        return minCostClimbingStairs(costs, 0)
