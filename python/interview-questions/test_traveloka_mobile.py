# 1. Easy Pattern


def easyPattern(n: int) -> str:
    rows = cols = (n * 2) - 1
    grid = [[" "] * rows for i in range(rows)]
    visited = set()

    def topDiag(row: int, col: int, ch: str):
        if row not in range(n) or col not in range(cols) or (row, col) in visited:
            return
        visited.add((row, col))
        grid[row][col] = ch
        topDiag(row + 1, col + 1, ch)

    def botDiag(row: int, col: int, ch: str):
        if row not in range(rows) or col not in range(n) or (row, col) in visited:
            return
        visited.add((row, col))
        grid[row][col] = ch
        botDiag(row + 1, col + 1, ch)

    ## top
    for row in range(n):
        for col in range(n):
            if (row, col) in visited:
                continue

            if row == 0 and col == n - 1:
                prev = "x"
                for temp_row in range(row, n, 2):
                    topDiag(temp_row, col, prev)
                    if prev == "x":
                        prev = "o"
                    elif prev == "o":
                        prev = "x"
            if col == 0 and row == n - 1:
                prev = "x"
                for temp_col in range(col, n, 2):
                    botDiag(row, temp_col, prev)
                    if prev == "x":
                        prev = "o"
                    elif prev == "o":
                        prev = "x"

    res = ["".join(grid[i]) for i in range(rows)]
    return "\n".join(res)


# actual_output = easyPattern(3)
# expected_output = [
#     "".join([" ", " ", "x", " ", " "]),
#     "".join([" ", " ", " ", "x", " "]),
#     "".join(["x", " ", "o", " ", "x"]),
#     "".join([" ", "x", " ", " ", " "]),
#     "".join([" ", " ", "x", " ", " "]),
# ]
# print(actual_output == "\n".join(expected_output))
# print()
# print(actual_output)
# print()

# actual_output = easyPattern(5)
# expected_output = [
#     "".join([" ", " ", " ", " ", "x", " ", " ", " ", " "]),
#     "".join([" ", " ", " ", " ", " ", "x", " ", " ", " "]),
#     "".join([" ", " ", " ", " ", "o", " ", "x", " ", " "]),
#     "".join([" ", " ", " ", " ", " ", "o", " ", "x", " "]),
#     "".join(["x", " ", "o", " ", "x", " ", "o", " ", "x"]),
#     "".join([" ", "x", " ", "o", " ", " ", " ", " ", " "]),
#     "".join([" ", " ", "x", " ", "o", " ", " ", " ", " "]),
#     "".join([" ", " ", " ", "x", " ", " ", " ", " ", " "]),
#     "".join([" ", " ", " ", " ", "x", " ", " ", " ", " "]),
# ]
# print(actual_output == "\n".join(expected_output))
# print()
# print(actual_output)
# print()


actual_output = easyPattern(10)
# expected_output = [
#     "".join([" ", " ", " ", " ", "x", " ", " ", " ", " "]),
#     "".join([" ", " ", " ", " ", " ", "x", " ", " ", " "]),
#     "".join([" ", " ", " ", " ", "o", " ", "x", " ", " "]),
#     "".join([" ", " ", " ", " ", " ", "o", " ", "x", " "]),
#     "".join(["x", " ", "o", " ", "x", " ", "o", " ", "x"]),
#     "".join([" ", "x", " ", "o", " ", " ", " ", " ", " "]),
#     "".join([" ", " ", "x", " ", "o", " ", " ", " ", " "]),
#     "".join([" ", " ", " ", "x", " ", " ", " ", " ", " "]),
#     "".join([" ", " ", " ", " ", "x", " ", " ", " ", " "]),
# ]
# print(actual_output == "\n".join(expected_output))
print(actual_output)
print()


# 2. Project Estimates
# - A number of bids are being taken for a project. Determine the number of distinct pairs of project costs where their absolute difference is some target value. Two pairs are distinct if they differ in at least one value.
# - Example
# 	- `n = 3`
# 	- `projectCosts = [1, 3, 5] target = 2`
# 	- There are 2 pairs `[1,3], [3,5]` that have the target difference `target = 2`, therefore a value of 2 is returned.
# - Function Description
# 	- countPairs has the following parameter(s):
# 	- int projectCosts[n]: array of integers
# 	- int target: the target difference
# - Returns
# 	- int: the number of distinct pairs in projectCosts with an absolute difference of target
# - Constraints
# 	- $5≤n≤105$
# 	- $0 < projectCosts[i] = 2 × 109$
# 	- Each projectCosts[i] is distinct, i.e. unique within projectCosts
# 	- $1 ≤ target ≤ 109$

# from typing import List


# def countPairs(projectCosts: List[int], target: int) -> int:
#     projectCosts.sort()
#     res = 0
#     left = 0
#     for right in range(1, len(projectCosts)):
#         diff = projectCosts[right] - projectCosts[left]
#         if diff == target:
#             res += 1
#             left += 1
#         elif diff > target:
#             left += 1
#
#     return res


# def countPairs(projectCosts: List[int], target: int) -> int:
#     map = {projectCost: i for i, projectCost in enumerate(projectCosts)}
#     res = 0
#
#     for projectCost in projectCosts:
#         diff = abs(projectCost - target)
#         diffPlus = projectCost + target
#         if diff in map:
#             res += 1
#         elif diffPlus in map:
#             res += 1
#         del map[projectCost]
#
#     return res


# input = [1, 3, 5]  # (1, 3), (3, 5)
# target = 2
# output = countPairs(projectCosts=input, target=target)
# print("actual: ", output, "expected: 2", output == 2)  # expected = 2
#
# input = [1, 5, 3, 4, 2]  # (1, 3), (2, 4), (3, 5)
# target = 2
# output = countPairs(projectCosts=input, target=target)
# print("actual: ", output, "expected: 3", output == 3)  # expected = 3
#
# input = [2, 4, 6, 8, 10, 12]  # (2, 4), (4, 6), (6, 8), (8, 10), (10, 12)
# target = 2
# output = countPairs(projectCosts=input, target=target)
# print("actual: ", output, "expected: 5", output == 5)  # expected = 5
# print()
