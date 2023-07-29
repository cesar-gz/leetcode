"""
74. Search a 2D Matrix

You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        topPtr, bottomPtr = 0, rows - 1

        while topPtr <= bottomPtr:
            middleRow = (topPtr + bottomPtr) // 2
            if target > matrix[middleRow][-1]:
                # if target value is greater than the right most value in row
                topPtr = middleRow + 1
            elif target < matrix[middleRow][0]:
                # if target value is less than the far left value in row
                bottomPtr = middleRow - 1
            else:
                break

        if not (topPtr <= bottomPtr):
            # value not in matrix
            return False

        # found the right row that the target is in
        row = (topPtr + bottomPtr) // 2
        leftPtr, rightPtr = 0, cols - 1
        while leftPtr <= rightPtr:
            middle = (leftPtr + rightPtr) // 2
            if target > matrix[row][middle]:
                leftPtr = middle + 1
            elif target < matrix[row][middle]:
                rightPtr = middle - 1
            else:
                return True
        return False
