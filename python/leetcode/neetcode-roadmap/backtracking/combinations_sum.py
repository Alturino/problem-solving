from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        combination = []

        def backtracking(start: int = 0, currSum: int = 0):
            if currSum == target:
                res.append(combination.copy())
                return

            if start >= len(candidates) or currSum > target:
                return

            combination.append(candidates[start])
            backtracking(start, currSum + candidates[start])
            combination.pop()
            backtracking(start + 1, currSum)

        backtracking()
        return res
