from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        cols = set()
        posDiag = set()
        negDiag = set()

        board = [["."] * n for i in range(n)]

        def backtracking(row: int):
            if row >= n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for col in range(n):
                if col in cols or (col + row) in posDiag or (col - row) in negDiag:
                    continue

                cols.add(col)
                posDiag.add(col + row)
                negDiag.add(col - row)
                board[row][col] = "Q"

                backtracking(row + 1)
                cols.remove(col)
                posDiag.remove(col + row)
                negDiag.remove(col - row)
                board[row][col] = "."

        backtracking(0)
        return res
