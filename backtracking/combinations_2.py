from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidate = []
        candidates.sort()

        def combination(start: int, curr: int):
            if curr == target:
                res.append(candidate.copy())
                return

            if curr > target or start >= len(candidates):
                return

            prev = -1
            for i in range(start, len(candidates)):
                if candidates[i] == prev:
                    continue
                candidate.append(candidates[i])
                combination(i + 1, curr + candidates[i])
                candidate.pop()
                prev = candidates[i]

        combination(0, 0)
        return res


s = Solution()
print(s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
