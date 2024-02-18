# 1. Easy Pattern


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

from typing import List


def countPairs(projectCosts: List[int], target: int) -> int:
    return 0


print(countPairs(projectCosts=[1, 5, 3, 4, 2], target=2))  # expected = 3
print(countPairs(projectCosts=[2, 4, 6, 8, 10, 12], target=2))  # expected = 5
print()
