from typing import List


class Solution:
    # def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    #     res = []
    #     combination = []
    #     candidates.sort()
    #
    #     def combinationSum(start: int, currTotal: int):
    #         if currTotal == target:
    #             res.append(combination.copy())
    #             return
    #
    #         if start >= len(candidates) or currTotal > target:
    #             return
    #
    #         prev = -1
    #         for i in range(start, len(candidates)):
    #             if candidates[i] == prev:
    #                 continue
    #             combination.append(candidates[i])
    #             combinationSum(i + 1, currTotal + candidates[i])
    #             combination.pop()
    #             prev = candidates[i]
    #
    #     combinationSum(0, 0)
    #     return res

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        combination = []
        candidates.sort()

        def combinationSum(start: int, currTotal: int):
            if currTotal == target:
                res.append(combination.copy())
                return

            if start >= len(candidates) or currTotal > target:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                combination.append(candidates[i])
                combinationSum(i + 1, currTotal + candidates[i])
                combination.pop()

        combinationSum(0, 0)
        return res
