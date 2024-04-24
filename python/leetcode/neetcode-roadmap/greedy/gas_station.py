from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        res = currGas = 0
        for i, gasi in enumerate(gas):
            currGas += gasi - cost[i]
            if currGas < 0:
                res = i + 1
                currGas = 0

        return res

    # def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    #     start, end = len(gas) - 1, 0
    #     total = gas[start] - cost[start]
    #
    #     while start >= end:
    #         while total < 0 and start >= end:
    #             start -= 1
    #             total += gas[start] - cost[start]
    #         if start == end:
    #             return start
    #         total += gas[end] - cost[end]
    #         end += 1
    #     return -1
