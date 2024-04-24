from collections import deque
from typing import List


class Solution:
    ## BFS
    # def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    #     rows, cols = len(grid), len(grid[0])
    #     visited = set()
    #
    #     def bfs(r, c):
    #         q = deque()
    #         visited.add((r, c))
    #         q.append((r, c))
    #
    #         area = 0
    #         while q:
    #             row, col = q.popleft()
    #             directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    #             for dr, dc in directions:
    #                 r, c = row + dr, col + dc
    #                 if (
    #                     (r) in range(rows)
    #                     and (c) in range(cols)
    #                     and grid[r][c] == 1
    #                     and (r, c) not in visited
    #                 ):
    #                     q.append((r, c))
    #                     visited.add((r, c))
    #                     area += 1
    #         return area
    #
    #     area = 0
    #     for r in range(rows):
    #         for c in range(cols):
    #             if grid[r][c] == 1 and (r, c) not in visited:
    #                 area = max(area, bfs(r, c))
    #     return area

    # DFS
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(row: int, col: int) -> int:
            if (
                row not in range(0, rows)
                or col not in range(0, cols)
                or grid[row][col] == 0
                or (row, col) in visited
            ):
                return 0

            visited.add((row, col))
            return (
                1
                + dfs(row + 1, col)
                + dfs(row - 1, col)
                + dfs(row, col + 1)
                + dfs(row, col - 1)
            )

        area = 0
        for r in range(rows):
            for c in range(cols):
                area = max(area, dfs(r, c))
        return area
