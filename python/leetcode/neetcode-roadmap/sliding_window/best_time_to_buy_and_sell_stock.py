from typing import List


class Solution:
    # def maxProfit(self, prices: List[int]) -> int:
    #     left, right = 0, 1
    #
    #     res = 0
    #     while right < len(prices):
    #         if prices[left] < prices[right]:
    #             res = max(res, (prices[right] - prices[left]))
    #         else:
    #             left = right
    #         right += 1
    #
    #     return res

    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        lowest = prices[0]

        for price in prices:
            lowest = min(lowest, price)
            res = max(res, (price - lowest))

        return res


s = Solution()
# prices = [7, 6, 4, 3, 1]
prices = [7, 1, 5, 3, 6, 4]
print(s.maxProfit(prices=prices))
