from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            if res[-1][1] >= intervals[i][0]:
                start, end = res.pop()
                res.append([min(start, intervals[i][0]), max(end, intervals[i][1])])
                continue
            res.append(intervals[i])
        return res


print(Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
print(Solution().merge([[1, 4], [0, 0]]))
