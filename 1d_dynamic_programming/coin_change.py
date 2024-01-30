from typing import List


class Solution:
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

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for coin in coins:
                if a - coin >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - coin])

        return dp[amount] if dp[amount] != amount + 1 else -1


s = Solution()
print(s.coinChange([1, 2, 5], 8))
