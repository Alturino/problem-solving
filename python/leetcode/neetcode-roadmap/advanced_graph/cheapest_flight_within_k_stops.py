# import heapq
# from typing import Dict, Tuple
from collections import defaultdict, deque
from typing import List


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
        for source, destination, price in flights:
            adj[source].append((destination, price))

        queue = deque([(src, 0, 0)])
        while queue:
            vertex, stops, price = queue.popleft()
            if stops > k:
                continue

            for vertex2, weight2 in adj[vertex]:
                if price + weight2 < prices[vertex2]:
                    prices[vertex2] = price + weight2
                    queue.append((vertex2, stops + 1, price + weight2))

        return -1 if prices[destination] == float("inf") else prices[destination]

    # Dijkstra
    # def findCheapestPrice(
    #     self,
    #     n: int,
    #     flights: List[List[int]],
    #     src: int,
    #     dst: int,
    #     k: int,
    # ) -> int:
    #     dist = [[float("inf")] * (k + 5) for _ in range(n)]
    #     adj: Dict[int, List[Tuple[int, int]]] = defaultdict(list)
    #     for source, to, price in flights:
    #         adj[source].append((price, to))
    #
    #     dist[src][0] = 0
    #     heap: List[Tuple[int, int, int]] = [(0, -1, src)]  # price, stops, source
    #     while heap:
    #         price, stops, source = heapq.heappop(heap)
    #         if dst == source:
    #             return price
    #         if stops == k or dist[source][stops + 1] < price:
    #             continue
    #
    #         for neighbor_price, neighbor in adj[source]:
    #             next_price = price + neighbor_price
    #             next_stops = stops + 1
    #             if dist[neighbor][next_stops + 1] > next_price:
    #                 dist[neighbor][next_stops + 1] = next_price
    #                 heapq.heappush(heap, (next_price, next_stops, neighbor))
    #
    #     return -1

    # Bellman Ford
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
