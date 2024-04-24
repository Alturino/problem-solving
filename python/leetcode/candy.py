from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        candy = [1] * len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candy[i] = candy[i - 1] + 1

        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candy[i] = max(candy[i], candy[i + 1] + 1)
        return sum(candy)


s = Solution()
print(s.candy(ratings=[1, 0, 2]))  # 5
print(s.candy(ratings=[1, 2, 2]))  # 4
print(s.candy(ratings=[1, 3, 2, 2, 1]))  # 8
print(s.candy(ratings=[1, 2, 87, 87, 87, 2, 1]))  # 13
print()
