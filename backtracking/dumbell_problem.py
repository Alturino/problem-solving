from copyreg import constructor
from typing import List

# a = [
#     [[1], [1]],
#     [[1, 1], [2]],
#     [[1, 1, 1], [3]],
#     [[1, 1, 2], [1, 3]],
#     [[1, 2], [3]],
# ]

# a = [
#     [[1], [1]],
#     [[1], [1]],
#     [[1], [1]],
#     [[1], [1]],
#     [[1], [1]],
#     [[1], [1]],
#     [[1, 1], [2]],
#     [[1, 1], [2]],
#     [[1, 1], [2]],
#     [[1, 1, 1], [3]],
#     [[1, 1, 2], [1, 3]],
#     [[1, 2], [3]],
#     [[1, 2], [3]],
#     [[1, 2], [3]],
#     [[1, 3], [1, 1, 2]],
#     [[2], [1, 1]],
#     [[2], [1, 1]],
#     [[2], [1, 1]],
#     [[3], [1, 1, 1]],
#     [[3], [1, 2]],
#     [[3], [1, 2]],
#     [[3], [1, 2]],
# ]


class Solution:
    def solve(self, plates: List[int]) -> List[List[int]]:
        res = []
        combination = []
        left = []
        right = []

        def backtracking(start: int, leftSum: int, rightSum: int):
            if left and right:
                if leftSum == rightSum:
                    combination.append(left.copy())
                    combination.append(right.copy())
                    res.append(combination.copy())
                    combination.clear()
                    return

            if start >= len(plates):
                return

            prev = -1
            for i in range(start, len(plates)):
                if prev == plates[i]:
                    continue
                left.append(plates[i])
                backtracking(i + 1, leftSum + plates[i], rightSum)
                left.pop()

                right.append(plates[i])
                backtracking(i + 1, leftSum, rightSum + plates[i])
                right.pop()

        backtracking(0, 0, 0)
        res.sort()
        return res


s = Solution()
print(s.solve([1, 1, 1, 2, 3]))
