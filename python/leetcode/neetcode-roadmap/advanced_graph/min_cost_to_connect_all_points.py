from typing import List, Tuple, Dict, Set
import heapq


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj: Dict[int, List[Tuple[int, int]]] = {i: [] for i in range(n)}

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append((dist, j))
                adj[j].append((dist, i))

        res = 0
        visited: Set[int] = set()
        heap = [(0, 0)]
        while len(visited) < n:
            dist, node = heapq.heappop(heap)
            if node in visited:
                continue

            res += dist
            visited.add(node)
            for neighbor_dist, neighbor in adj[node]:
                if neighbor not in visited:
                    heapq.heappush(heap, (neighbor_dist, neighbor))
        return res
