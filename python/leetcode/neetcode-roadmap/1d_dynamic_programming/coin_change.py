from typing import List


class Solution:
    # Iterative dp bottom-up
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for coin in coins:
                if a - coin >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - coin])

        return dp[amount] if dp[amount] != amount + 1 else -1

    # # Recursive dp memoization bottom-up
    # def coinChange(self, coins: List[int], amount: int):
    #     minCount = float("inf")
    #     dp = [0] * (amount + 1)
    #
    #     def backtracking(start: int, currAmount: int, currCoinCount: int):
    #         nonlocal minCount
    #         if currAmount == amount:
    #             minCount = min(minCount, currCoinCount)
    #             return
    #
    #         if start >= len(coins) or currAmount > amount:
    #             return
    #
    #         dp[currAmount] = currCoinCount
    #         for i in range(len(coins)):
    #             backtracking(i, currAmount + coins[i], currCoinCount + 1)
    #
    #     backtracking(0, 0, 0)
    #     return minCount

    # # Recursive top-down memoization
    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     cache = {}
    #
    #     def rec(curr_amount: int = amount) -> int:
    #         if curr_amount == 0:
    #             return 0
    #         if curr_amount in cache:
    #             return cache[curr_amount]
    #
    #         res = 1 << 64
    #         for coin in coins:
    #             if curr_amount - coin >= 0:
    #                 res = min(res, 1 + rec(curr_amount - coin))
    #         cache[curr_amount] = res
    #         return res
    #
    #     res = rec()
    #     return res if res != 1 << 64 else -1

    # # Recursive top-down
    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     def rec(curr_amount: int = amount) -> int:
    #         if curr_amount == 0:
    #             return 0
    #
    #         res = 1 << 64
    #         for coin in coins:
    #             if curr_amount - coin >= 0:
    #                 res = min(res, 1 + rec(curr_amount - coin))
    #         return res
    #
    #     res = rec()
    #     return res if res != 1 << 64 else -1


s = Solution()
print(s.coinChange([1, 2, 5], 8))
