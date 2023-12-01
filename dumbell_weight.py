from typing import List

# Input
input = [1, 1, 1, 2, 3]

# Expected Output
# [
#     [[1], [1]],
#     [[1, 1], [2]],
#     [[1, 1, 1], [3]],
#     [[1, 1, 2], [3, 1]],
#     [[1, 2], [3]],
#     [[1], [1]],
#     [[2], [1, 1]],
#     [[3], [1, 1, 1]],
#     [[3, 1], [1, 1, 2]],
#     [[3], [1, 2]],
# ]

# Actual Output
# [
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


a = [
    [[1, 1, 1], [3]],
    [[1, 1, 2], [1, 3]],
    [[1, 1], [2]],
    [[1], [1]],
    [[1, 1], [2]],
    [[1], [1]],
    [[1, 2], [3]],
    [[1, 1], [2]],
    [[1], [1]],
    [[1, 2], [3]],
    [[1, 2], [3]],
]


def solve(plates: List[int]):
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

        for i in range(start, len(plates)):
            left.append(plates[i])
            backtracking(i + 1, leftSum + plates[i], rightSum)
            left.pop()

            right.append(plates[i])
            backtracking(i + 1, leftSum, rightSum + plates[i])
            right.pop()

    backtracking(0, 0, 0)
    return res


print(solve(input))
