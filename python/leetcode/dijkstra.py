from typing import List, Dict
import collections
import heapq


class Solution:
    def minimumWeightToDestination(
        self, n: int, edges: List[List[int]], src: int
    ) -> Dict[int, int]:  # vertex: weight
        adj = collections.defaultdict(list)
        for source, destination, weight in edges:
            adj[source].append((weight, destination))

        shortest = {}
        minHeap = [(0, src)]  # weight, vertex
        while minHeap:
            weight1, vertex1 = heapq.heappop(minHeap)
            if vertex1 in shortest:
                continue

            shortest[vertex1] = weight1
            for weight2, vertex2 in adj[vertex1]:
                if vertex2 not in shortest:
                    heapq.heappush(minHeap, (weight1 + weight2, vertex2))

        for i in range(n):
            if i not in shortest:
                shortest[i] = -1

        return shortest
