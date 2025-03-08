from collections import defaultdict
from typing import List
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)
        for source, destination, time in times:
            adj_list[source].append((destination, time))

        heap = [(0, k)]
        visited = set()
        res = 0
        while heap:
            time, vertex = heapq.heappop(heap)
            if vertex in visited:
                continue
            visited.add(vertex)
            res = time

            for vertex2, time2 in adj_list[vertex]:
                if vertex2 not in visited:
                    heapq.heappush(heap, (time + time2, vertex2))
        return res if len(visited) == n else -1


s = Solution()
# print(s.networkDelayTime(times=[[2, 1, 1], [2, 3, 1], [3, 4, 1]], n=4, k=2))
print(s.networkDelayTime(times=[[1, 2, 1], [2, 1, 3]], n=4, k=2))
