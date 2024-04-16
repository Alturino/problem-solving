from typing import List


class Solution:
    # def insert(
    #     self,
    #     intervals: List[List[int]],
    #     newInterval: List[int],
    # ) -> List[List[int]]:
    #     res = []
    #     n = len(intervals)
    #     i = 0
    #
    #     while i < n and intervals[i][1] < newInterval[0]:
    #         res.append(intervals[i])
    #         i += 1
    #
    #     while i < n and intervals[i][0] <= newInterval[1]:
    #         newInterval[0], newInterval[1] = (
    #             min(newInterval[0], intervals[i][0]),
    #             max(newInterval[1], intervals[i][1]),
    #         )
    #         i += 1
    #     res.append(newInterval)
    #
    #     while i < n:
    #         res.append(intervals[i])
    #         i += 1
    #     return res

    def insert(
        self,
        intervals: List[List[int]],
        newInterval: List[int],
    ) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            if intervals[i][0] > newInterval[1]:
                res.append(newInterval)
                return res + intervals[i:]
            elif intervals[i][1] < newInterval[0]:
                res.append(intervals[i])
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1]),
                ]
        res.append(newInterval)
        return res
