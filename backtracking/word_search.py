from typing import List
from typing import Counter
import collections


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set()

        def exist(row: int, col: int, currWordIndex: int):
            if currWordIndex == len(word):
                return True

            if (
                min(row, col) < 0
                or row >= rows
                or col >= rows
                or board[row][col] != word[currWordIndex]
                or (row, col) in visited
            ):
                return False

            visited.add((row, col))
            res = (
                exist(row + 1, col, currWordIndex + 1)
                or exist(row - 1, col, currWordIndex + 1)
                or exist(row, col + 1, currWordIndex + 1)
                or exist(row, col - 1, currWordIndex + 1)
            )
            visited.remove((row, col))
            return res

        count = collections.defaultdict(int, sum(map(Counter, board), Counter()))
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]

        for row in range(rows):
            for col in range(cols):
                if exist(col, row, 0):
                    return True

        return False


s = Solution()
print(
    s.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE")
)
