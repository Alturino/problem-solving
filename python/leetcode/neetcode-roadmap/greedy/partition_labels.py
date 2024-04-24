from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        m = {}
        for i, c in enumerate(s):
            m[c] = i

        size, end = 0, 0
        res = []
        for i, c in enumerate(s):
            size += 1
            end = max(end, m[c])

            if i == end:
                res.append(size)
                size = 0

        return res
