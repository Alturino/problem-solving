from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        combination = []

        def backtracking(curr: int):
            if len(combination) == k:
                res.append(combination.copy())
                return

            if curr not in range(n + 1):
                return

            for i in range(curr, n + 1):
                combination.append(i)
                backtracking(curr + 1)
                combination.pop()
                curr = i + 1

        backtracking(1)
        return res


s = Solution()
print(s.combine(4, 2))
