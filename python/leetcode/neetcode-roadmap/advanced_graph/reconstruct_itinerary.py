from typing import Deque, Dict, List
from collections import defaultdict, deque


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        

    # def findItinerary(self, tickets: List[List[str]]) -> List[str]:
    #     tickets.sort()
    #     adj: Dict[str, List[str]] = defaultdict(list)
    #     for source, destination in tickets:
    #         adj[source].append(destination)
    #
    #     res = ["JFK"]
    #
    #     def dfs(source: str = "JFK") -> bool:
    #         if len(res) == len(tickets) + 1:
    #             return True
    #         if source not in adj:
    #             return False
    #
    #         temp = list(adj[source])
    #         for i, destination in enumerate(temp):
    #             adj[source].pop(i)
    #             res.append(destination)
    #             if dfs(destination):
    #                 return True
    #             adj[source].insert(i, destination)
    #             res.pop()
    #         return False
    #
    #     dfs()
    #     return res


s = Solution()
print(
    s.findItinerary(
        tickets=[["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    )
)
print(
    s.findItinerary(
        tickets=[
            ["JFK", "SFO"],
            ["JFK", "ATL"],
            ["SFO", "ATL"],
            ["ATL", "JFK"],
            ["ATL", "SFO"],
        ]
    )
)
