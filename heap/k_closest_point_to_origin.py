import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            distance = (x**2) + (y**2)
            heap.append([distance, x, y])
        heapq.heapify(heap)

        res = []
        for i in range(k):
            distance, x, y = heapq.heappop(heap)
            res.append([x, y])
        return res
