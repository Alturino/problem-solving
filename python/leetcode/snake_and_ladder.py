from typing import List
import collections


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        board.reverse()

        def squareToRowCol(square: int) -> List[int]:
            r = (square - 1) // n
            c = (square - 1) % n
            if r % 2:
                c = n - 1 - c
            return [r, c]

        q = collections.deque()
        q.append([1, 0])
        visited = set()
        while q:
            square, moves = q.popleft()
            for i in range(1, 7):
                newSquare = square + i
                r, c = squareToRowCol(newSquare)
                if board[r][c] != -1:
                    newSquare = board[r][c]
                if newSquare == n * n:
                    return moves + 1
                if newSquare not in visited:
                    visited.add(newSquare)
                    q.append([newSquare, moves + 1])
        return -1
