from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zeros = []
        for temp in range(len(matrix)):
            for col in range(len(matrix[temp])):
                if matrix[temp][col] == 0:
                    zeros.append([temp, col])

        for row, col in zeros:
            for temp in range(row + 1, len(matrix)):
                matrix[temp][col] = 0
            for temp in range(col + 1, len(matrix[row])):
                matrix[row][temp] = 0
            for temp in range(len(matrix[row]) - 1, -1, -1):
                matrix[row][temp] = 0
            for temp in range(len(matrix) - 1, -1, -1):
                matrix[temp][col] = 0

        return


s = Solution()
print(s.setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
