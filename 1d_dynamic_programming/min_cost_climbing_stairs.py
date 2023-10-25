from typing import List
class Solution:
    # # Recursive
    # def minCostClimbingStairs(self, costs: List[int]) -> int:
    #     def minCostClimbingStairs(costs: List[int], curr: int) -> int: 
    #         if curr >= len(costs) or curr < 0:
    #             return 0
    #         if curr <= 1:
    #             return costs[curr]
    #         return costs[curr] + min(minCostClimbingStairs(costs, curr - 1, memo), minCostClimbingStairs(costs, curr - 2, memo))
    #     takeOneStep = minCostClimbingStairs(costs, len(costs) - 1)
    #     takeTwoStep = minCostClimbingStairs(costs, len(costs) - 2)
    #     return min(takeOneStep, takeTwoStep)

    # # Recursive with memoization
    # def minCostClimbingStairs(self, costs: List[int]) -> int:
    #     memo= {}
    #     def minCostClimbingStairs(costs: List[int], curr: int, memo) -> int: 
    #         if curr >= len(costs) or curr < 0:
    #             memo[curr] = 0
    #             return memo[curr]
    #         if curr <= 1:
    #             memo[curr] = costs[curr]
    #             return memo[curr]
    #         if curr in memo:
    #             return memo[curr]
    #         memo[curr] = costs[curr] + min(minCostClimbingStairs(costs, curr - 1, memo), minCostClimbingStairs(costs, curr - 2, memo))
    #         return memo[curr]
    #     takeOneStep = minCostClimbingStairs(costs, len(costs) - 1, memo)
    #     takeTwoStep = minCostClimbingStairs(costs, len(costs) - 2, memo)
    #     return min(takeOneStep, takeTwoStep)

    # # Iterative from last
    # def minCostClimbingStairs(self, costs: List[int]) -> int:
    #     for i in range(len(costs) - 3, -1 , -1):
    #         costs[i] += min(costs[i + 1], costs[i + 2])
    #     print(costs)
    #     return min(costs[0], costs[1])

    # Iterative from last
    def minCostClimbingStairs(self, costs: List[int]) -> int:
        one, two = 0, 0
        for i in range(len(costs) - 1, -1, -1):
            costs[i] += min(one, two)
            two = one
            one = costs[i]
        return min(costs[0], costs[1])

s = Solution()
print(s.minCostClimbingStairs([10, 15, 20]))

