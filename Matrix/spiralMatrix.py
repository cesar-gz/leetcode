"""
54. Spiral Matrix

Given an m x n matrix, return all elements of the matrix in spiral order.
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # solve by creating pointers, pointing to each boundary
        # left pointer points to left corner, right to right corner . . .
        result = []
        leftPtr, rightPtr = 0 , len(matrix[0]) # number of cols
        topPtr, bottomPtr = 0, len(matrix) # number of rows

        while leftPtr < rightPtr and topPtr < bottomPtr:
            # first go left to right and get every value in the top row
            for i in range(leftPtr, rightPtr):
                result.append(matrix[topPtr][i])

            # shift top boundary down 1 row
            topPtr += 1

            # get every in the right col
            for i in range(topPtr, bottomPtr):
                result.append(matrix[i][rightPtr - 1]) # subtract by 1 because we are out of bounds

            # shift right boundary to the left 1 column
            rightPtr -= 1

            if not (leftPtr < rightPtr and topPtr < bottomPtr):
                # edge case for input matrixes that are more columnar then square
                break

            # get every i in the bottom row, go right to left in reverse order
            for i in range(rightPtr -1, leftPtr -1, -1):
                result.append(matrix[bottomPtr -1][i])

            # shift bottomPtr upwards 1 row
            bottomPtr -= 1

            # get every i in the left column
            for i in range(bottomPtr -1, topPtr -1, -1):
                result.append(matrix[i][leftPtr])

            # shift left boundary to the right by 1 column
            leftPtr += 1

        return result
        # O(m*n) time, O(1) space
