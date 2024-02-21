# 1. Slowest Key Press
# - Engineers have redesigned a keypad used by ambulance drivers in urban areas. In order to determine which key takes the longest time to press, the keypad is tested by a driver. Given the results of that test, determine which key takes the longest to press.
# - Example
# 	- `keyTimes = [[0,2], [1, 5], [0, 9], [2, 15]]`
# 	- Elements in `keyTimes[i][0]` represent encoded characters in the range `ascii[a-z]` where`a = 0` , `b = 1`, ..., `z = 25.`
# 	- The second element, `keyTimes[i][1]` represents the time the key is pressed since the start of the test.
# 	- The elements will be given in ascending time order. In the example, keys pressed, in order are `0102[encoded] = abac` at times `2, 5, 9, 15`. From the start time, it took `2-0 = 2` to press the first key,`5-2=3`  to press the second, and so on. The longest time it took to press a key was key `2`, or `'c'`, at `15 - 9 = 6`.
# - Function Description
# 	- slowestKey has the following parameter(s):
# 		- `int keyTimes[n][2]`: the first column contains the encoded key pressed, the second contains the time at which it was pressed
# - Returns:
# 	- char: the key that took the longest time to press
# - Constraints
# 	- $1≤n≤ 105$
# 	- $0 ≤ keyTimes[i][0] ≤ 25 (0 ≤ i ≤n)$
# 	- $1 ≤ keyTimes[i][1] ≤ 10° (0 ≤i≤n)$
# 	- There will only be one key with the worst time.
# 	- $keyTimes$ is sorted in ascending order of $keyTimes[i][1]$

from typing import List
import collections


def slowestKey(keyTimes: List[List[int]]) -> str:
    key, time = keyTimes[0][0], keyTimes[0][1]
    for i in range(1, len(keyTimes)):
        currTime = keyTimes[i][1] - keyTimes[i - 1][1]
        if time < currTime:
            key = keyTimes[i][0]
            time = currTime
        elif currTime == time:
            key = max(key, keyTimes[i][0])

    return chr(key + ord("a"))


print(slowestKey(keyTimes=[[0, 2], [1, 3], [0, 7]]))  # expected = 'a'
print(slowestKey(keyTimes=[[0, 1], [0, 3], [4, 5], [5, 6], [4, 10]]))  # expected = 'e'
print()


# 2. The Jungle Book
# - There are a number of animal species in the jungle. Each species has one or more predators that may be direct or indirect. Species X is said to be a predator of species Y if at least one of the following is true
# 	- Species X is a direct predator of species Y.
# 	- If species X is a direct predator of species Z, and Z is a direct predator of Y, then species Xis an indirect predator of species Y. Indirect predation is transitive through any number of levels
# - Each species has a maximum of 1 direct predator. No two species will ever be mutual predators, and no species is a predator of itself. Determine the minimum number of groups that must be formed to so that no species is grouped with its predators, direct or indirect.
# - Example
# 	- predators = [-1, 8, 6, 0, 7, 3, 8, 9, -1, 6]
# 	- Each position in predators represents a species and each element represents a predator of that species, or -1 if there are none. The graph of predation is below using zero based indexing. All labels are the indices within predators.
# - From the graph, a possible grouping is
# 	- [0,8]
# 	- [3,1,6]
# 	- [5,2,9]
# 	- [7]
# 	- [4]
# - A minimum of 5 groups are needed to satisfy all conditions.
# - Function Description
# - Complete the function minimumGroups in the editor below. minimumGroups has the following parameter(s):
# 	- int predators[n]: an array of integers where predator[i] represents the direct predator of the ith species or -1 if there is none.
# - Returns:
# 	- int: the minimum number of groups formed given the rule that none of the species will associate with its predators
# - Constraints:
# 	- $1 ≤ n ≤ 103$
# 	- $-1 ≤ predators[i] < n$
# 	- $predators[i] \neq i$


# def minimumGroups(predators: List[int]) -> int:
#     adjList = collections.defaultdict(list)
#     for i, predator in enumerate(predators):
#         adjList[predator].append(i)
#
#     groups = []
#     q = collections.deque(adjList[-1])
#     while q:
#         group = []
#         for i in range(len(q)):
#             node = q.popleft()
#             group.append(node)
#             if node in adjList:
#                 children = adjList[node]
#                 for child in children:
#                     q.append(child)
#         groups.append(group.copy())
#
#     return len(groups)
#
#
# print(minimumGroups(predators=[-1, 8, 6, 0, 7, 3, 8, 9, -1, 6]) == 5)  # expected = 5
# print(minimumGroups(predators=[-1, 0, 1]) == 3)  # expected = 3
# print(minimumGroups(predators=[1, -1, 3, -1]) == 2)  # expected = 2
# print()

# 3. Ways to Sum
# - An automated packaging system is responsible for packing boxes. A box is certified to hold a certain weight. Given an integer total, calculate the number of possible ways to achieve total as a sum of the weights of items weighing integer weights from 1 to k, inclusive.
# - Example
# 	- `total = 8`
# 	- `*k = 2*`
# 	- To reach a weight of 8, there are 5 different ways that items with weights between 1 and 2 can be combined:
# 		- [1, 1, 1, 1, 1, 1, 1, 1]
# 		- [1, 1, 1, 1, 1, 1, 2]
# 		- [1, 1, 1, 1, 2, 2]
# 		- [1, 1, 2, 2, 2]
# 		- [2, 2, 2, 2]
# - Function Description
# 	- ways has the following parameter(s):
# 		- `int total`: the value to sum to
# 		- `int k`: the maximum of the range of integers to consider when summing to total
# - Returns
# 	- int: the number of ways to sum to the total; the number might be very large, so return the integer modulo 1000000007 (109+7)
# - Constraints
# 	- $1 ≤ total ≤ 1000$
# 	- $1 ≤ k ≤ 100$


# def ways(total: int, k: int) -> int:
#     res = []
#     curr = []
#     m = {}
#
#     def backtrack(n: int, k: int):
#         if n == 0:
#             res.append(curr.copy())
#             return
#
#         if n < 0 or k <= 0:
#             return
#
#         curr.append(k)
#         backtrack(n - k, k)
#         curr.pop()
#         backtrack(n, k - 1)
#
#     backtrack(total, k)
#     return len(res)


# def ways(total: int, k: int, m={}) -> int:
#     if total == 0:
#         return 1
#
#     if total < 0 or k <= 0:
#         return 0
#
#     return ways(total - k, k, m) + ways(total, k - 1, m)


def ways(total: int, k: int, m={}) -> int:
    if (total, k) in m:
        return m[(total, k)]

    if total == 0:
        return 1

    if total < 0 or k <= 0:
        return 0

    res = ways(total - k, k, m) + ways(total, k - 1, m)
    m[(total, k)] = res
    return res


# def ways(total: int, k: int) -> int:
#     dp = [0] * (total + 1)
#     dp[0] = 1
#     for i in range(1, k + 1):
#         for j in range(1, total + 1):
#             if j >= i:
#                 dp[j] += dp[j - i]
#     return dp[total]


print(ways(total=8, k=2))  # expected = 5
print(ways(total=5, k=3))  # expected = 5
print(ways(total=4, k=2))  # expected = 3 [1,1,1,1], [1,1,2], [2,2]
print()
