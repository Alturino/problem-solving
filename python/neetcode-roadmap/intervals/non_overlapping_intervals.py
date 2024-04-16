from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        res = 0
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(prevEnd, end)
        return res


s = Solution()
print(s.eraseOverlapIntervals(intervals=[[1, 2], [1, 3], [2, 3], [3, 4]]))  # 1
print(s.eraseOverlapIntervals(intervals=[[1, 2], [1, 2], [1, 2]]))  # 2
print(s.eraseOverlapIntervals(intervals=[[1, 2], [2, 3]]))  # 0
print(s.eraseOverlapIntervals(intervals=[[1, 11], [1, 100], [2, 12], [11, 22]]))  # 2
print()
