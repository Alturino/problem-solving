from typing import List


class Solution:
    # # Recursive
    # def minCostClimbingStairs(self, costs: List[int]) -> int:
    #     def minCostClimbingStairs(costs: List[int], curr: int) -> int:
    #         if curr >= len(costs) or curr < 0:
    #             return 0
    #         if curr <= 1:
    #             return costs[curr]
    #         return costs[curr] + min(minCostClimbingStairs(costs, curr - 1), minCostClimbingStairs(costs, curr - 2))
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

    # # Iterative from last
    # def minCostClimbingStairs(self, costs: List[int]) -> int:
    #     one, two = 0, 0
    #     for i in range(len(costs) - 1, -1, -1):
    #         costs[i] += min(one, two)
    #         two = one
    #         one = costs[i]
    #     return min(costs[0], costs[1])

    # # Recursive from beginning
    # def minCostClimbingStairs(self, costs: List[int]) -> int:
    #     n = len(costs)
    #
    #     def minCostClimbingStairs(n: int) -> int:
    #         if n < 0:
    #             return 0
    #
    #         if n == 0 or n == 1:
    #             return costs[n]
    #
    #         return costs[n] + min(
    #             minCostClimbingStairs(n - 1), minCostClimbingStairs(n - 2)
    #         )
    #
    #     return min(minCostClimbingStairs(n - 1), minCostClimbingStairs(n - 2))

    # # Recursive memoization from beginning
    # def minCostClimbingStairs(self, costs: List[int]) -> int:
    #     n = len(costs)
    #     memo = {}
    #
    #     def minCostClimbingStairs(n: int) -> int:
    #         if n < 0:
    #             memo[n] = 0
    #             return 0
    #
    #         if n == 0 or n == 1:
    #             memo[n] = costs[n]
    #             return costs[n]
    #
    #         if n in memo:
    #             return memo[n]
    #
    #         res = costs[n] + min(
    #             minCostClimbingStairs(n - 1), minCostClimbingStairs(n - 2)
    #         )
    #         memo[n] = res
    #         return res
    #
    #     return min(minCostClimbingStairs(n - 1), minCostClimbingStairs(n - 2))

    # # Iterative tabulation from beginning
    # def minCostClimbingStairs(self, costs: List[int]) -> int:
    #     n = len(costs)
    #     dp = [0] * (n + 1)
    #     dp[0] = costs[0]
    #     dp[1] = costs[1]
    #
    #     for i in range(2, n):
    #         dp[i] = costs[i] + min(dp[i - 1], dp[i - 2])
    #     return min(dp[n - 1], dp[n - 2])

    # # Iterative from beginning
    # def minCostClimbingStairs(self, costs: List[int]) -> int:
    #     n = len(costs)
    #
    #     first, second = costs[0], costs[1]
    #     if n <= 2:
    #         return min(first, second)
    #
    #     for i in range(2, n):
    #         temp = costs[i] + min(first, second)
    #         first = second
    #         second = temp
    #
    #     return min(first, second)


s = Solution()
print(s.minCostClimbingStairs([10, 15, 20]))
