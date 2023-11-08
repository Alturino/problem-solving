from typing import Optional
from typing import List
import copy

class Node:
    def __init__(self, val, neighbors: List[Optional['Node']]):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# class Solution:
#     def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
#         visited = {}
#
#         def dfs(node: Optional['Node']) -> Optional['Node']:
#             if not node:
#                 return None
#             
#             if node in visited:
#                 return visited[node]
#
#             copy = Node(node.val, neighbors=[])
#             visited[node] = copy
#
#             for neighbor in node.neighbors:
#                 copy.neighbors.append(dfs(neighbor))
#             return copy
#
#         return dfs(node) if node else None

# class Solution:
#     def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
#         if not node:
#             return
#         
#         visited = {node.val: Node(node.val, neighbors=[])}
#         q = deque()
#         q.append(node)
#         
#         while q:
#             current = q.popleft()
#             currentCopy = Node(current.val, neighbors=[])
#
#             for neighbor in current.neighbors:
#                 if neighbor.val not in visited:
#                     visited[neighbor.val] = Node(neighbor.val, neighbors=[])
#                     q.append(neighbor)
#                 currentCopy.neighbors.append(visited[neighbor.val])
#                 
#         return visited[node.val]


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        return copy.deepcopy(node)

