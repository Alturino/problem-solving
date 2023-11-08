class Solution:
    def aWaysToSum(self, total, k):
        if total == 0:
            return 1

        if total < 0 or k <= 0:
            return 0

        return self.aWaysToSum(total - k, k) + self.aWaysToSum(total, k - 1)

    # def aWaysToSum(self, total, k):
    #     dp = [0] * (total + 1)
    #     dp[0] = 1
    #     for i in range(1, k + 1):
    #         for j in range(1, total + 1):
    #             if j >= i:
    #                 dp[j] += dp[j - i]
    #
    #     return dp[total]


s = Solution()
print(s.aWaysToSum(4, 2))
