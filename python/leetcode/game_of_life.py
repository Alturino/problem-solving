from typing import List

# | Original | New | State |
# | -------- | --- | ----- |
# | 0        | 0   | 0     |
# | 1        | 0   | 1     |
# | 0        | 1   | 2     |
# | 1        | 1   | 3     |

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        rl, cl = len(board), len(board[0])

        def countNeighbors(row: int, col: int) -> int:
            neighbor = 0
            for i in range(row - 1, row + 2):
                for j in range(col - 1, col + 2):
                    if (
                        (i == row and j == col)
                        or i not in range(rl)
                        or j not in range(cl)
                    ):
                        continue
                    if board[i][j] in set([1, 3]):
                        neighbor += 1
            return neighbor

        for row in range(rl):
            for col in range(cl):
                neighbor = countNeighbors(row, col)
                if board[row][col]:
                    if neighbor in set([2, 3]):
                        board[row][col] = 3
                elif neighbor == 3:
                    board[row][col] = 2

        for row in range(rl):
            for col in range(cl):
                if board[row][col] == 1:
                    board[row][col] = 0
                elif board[row][col] in set([2, 3]):
                    board[row][col] = 1
