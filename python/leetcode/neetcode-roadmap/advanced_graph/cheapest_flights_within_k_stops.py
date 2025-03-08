from typing import List
from collections import defaultdict
from collections import deque


class Solution:
    def findCheapestPrice(
        self,
        n: int,
        flights: List[List[int]],
        src: int,
        destination: int,
        k: int,
    ) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        adj = defaultdict(list)
        for s, d, weight in flights:
            adj[s].append((d, weight))

        queue = deque([(src, 0, 0)])
        while queue:
            vertex, stops, weight = queue.popleft()
            if stops > k:
                continue

            for vertex2, weight2 in adj[vertex]:
                if weight + weight2 < prices[vertex2]:
                    prices[vertex2] = weight + weight2
                    queue.append((vertex2, stops + 1, weight + weight2))

        return -1 if prices[destination] == float("inf") else prices[destination]

    # def findCheapestPrice(
    #     self,
    #     n: int,
    #     flights: List[List[int]],
    #     src: int,
    #     destination: int,
    #     k: int,
    # ) -> int:
    #     prices = [float("inf")] * n
    #     prices[src] = 0
    #
    #     for i in range(k + 1):
    #         temp_prices = prices.copy()
    #         for s, d, p in flights:
    #             if prices[s] == float("inf"):
    #                 continue
    #             if prices[s] + p < temp_prices[d]:
    #                 temp_prices[d] = prices[s] + p
    #         prices = temp_prices
    #
    #     return -1 if prices[destination] == float("inf") else prices[destination]
