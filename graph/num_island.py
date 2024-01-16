from collections import deque
from typing import List


class Solution:
    ## BFS
    # def numIsland(self, grid: List[List[str]]) -> int:
    #     if not grid:
    #         return 0
    #
    #     rows, cols = len(grid), len(grid[0])
    #     visited = set()
    #     islands = 0
    #
    #     def bfs(r, c):
    #         q = deque()
    #         visited.add((r, c))
    #         q.append((r, c))
    #
    #         while q:
    #             row, col = q.popleft()
    #             directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    #             for dr, dc in directions:
    #                 r, c = row + dr, col + dc
    #                 if (
    #                     (r) in range(rows)
    #                     and (c) in range(cols)
    #                     and grid[r][c] == "1"
    #                     and (r, c) not in visited
    #                 ):
    #                     q.append((r, c))
    #                     visited.add((r, c))
    #
    #     for r in range(rows):
    #         for c in range(cols):
    #             if grid[r][c] == "1" and (r, c) not in visited:
    #                 visited.add(grid[r][c])
    #                 bfs(r, c)
    #                 islands += 1
    #     return islands

    # DFS
    def numIsland(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(row: int, col: int):
            if (
                row not in range(0, rows)
                or col not in range(0, cols)
                or grid[row][col] == "0"
                or (row, col) in visited
            ):
                return

            visited.add((row, col))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for direction_row, direction_col in directions:
                dfs(row + direction_row, col + direction_col)

        islandCount = 0
        for row in range(rows):
            for col in range(cols):
                if (row, col) in visited or grid[row][col] == "0":
                    continue
                islandCount += 1
                dfs(row, col)

        return islandCount
