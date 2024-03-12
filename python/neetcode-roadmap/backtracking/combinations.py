from typing import List


class Solution:
    # def combinations(self, n: int, k: int) -> List[List[int]]:
    #     res = []
    #
    #     def combinations(start: int, comb: List[int]):
    #         if len(comb) == k:
    #             res.append(comb.copy())
    #             return
    #         for i in range(start, n + 1):
    #             comb.append(i)
    #             combinations(i + 1, comb)
    #             comb.pop()
    #
    #     combinations(1, [])
    #     return res

    def combinations(self, n: int, k: int) -> List[List[int]]:
        res = []
        combination = []

        def backtracking(start: int = 1):
            if len(combination) >= k:
                res.append(combination.copy())
                return

            for i in range(start, n + 1):
                combination.append(i)
                backtracking(i + 1)
                combination.pop()

        backtracking()
        return res


s = Solution()
print(s.combinations(4, 2))
print()
