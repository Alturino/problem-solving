from typing import List


class Solution:
    ## Time Complexity O(M Log N)
    ## Space Complexity O(1)
    # def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    #     for row in matrix:
    #         left, right = 0, len(row) - 1
    #
    #         if row[right] < target:
    #             continue
    #
    #         if row[right] == target:
    #             return True
    #         elif row[left] == target:
    #             return True
    #
    #         while left <= right:
    #             mid = left + ((right - left) // 2)
    #             if row[mid] < target:
    #                 left = mid + 1
    #             elif row[mid] > target:
    #                 right = mid - 1
    #             else:
    #                 return True
    #
    #     return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        # Binary search by row
        top, bottom = 0, rows - 1
        while top <= bottom:
            row = (top + bottom) // 2
            if matrix[row][-1] < target:
                top = row + 1
            elif matrix[row][0] > target:
                bottom = row - 1
            else:
                break

        if not top <= bottom:
            return False

        # Binary search by column when the row is exist
        row = top + ((bottom - top) // 2)
        left, right = 0, cols - 1
        while left <= right:
            mid = left + ((right - left) // 2)
            if matrix[row][mid] < target:
                left = mid + 1
            elif matrix[row][mid] > target:
                right = mid - 1
            else:
                return True

        return False
