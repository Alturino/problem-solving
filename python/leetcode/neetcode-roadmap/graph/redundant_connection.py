import collections
from typing import List, Set


class Solution:
    # # DFS
    # # O(N^2)
    # def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
    #     graphAsAdjancyList = collections.defaultdict(list)
    #
    #     def isCycleDfs(n1: int, n2: int, visited: Set[int]) -> bool:
    #         if n1 in visited:
    #             return False
    #
    #         if n1 == n2:
    #             return True
    #
    #         visited.add(n1)
    #         for i in graphAsAdjancyList.get(n1, []):
    #             if isCycleDfs(i, n2, visited):
    #                 return True
    #         return False
    #
    #     for n1, n2 in edges:
    #         if isCycleDfs(n1, n2, set()):
    #             return [n1, n2]
    #         graphAsAdjancyList[n1].append(n2)
    #         graphAsAdjancyList[n2].append(n1)
    #     return []

    # Union Find
    # O(N)
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(n: int) -> int:
            p = parent[n]

            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p

        def union(n1: int, n2: int) -> bool:
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]

        return []


s = Solution()
print(s.findRedundantConnection(edges=[[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]))
