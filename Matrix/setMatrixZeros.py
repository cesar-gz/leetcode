"""
73. Set Matrix Zeroes

Given an m x n int matrix, if an element is 0, set its entire row and column to 0s.
You must do it in place.
"""

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        is_col_zero = False
        R = len(matrix)
        C = len(matrix[0])
        for i in range(R):
            # use an additional var for the first column
            # and using matrix[0][0] for the first row
            if matrix[i][0] == 0:
                is_col_zero = True
            for j in range(1, C):
                # if an elem is zero, we set the first elem of the corresponding row and col to 0
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        # iterate over the array once again and using the first row and first col, update the elems
        for i in range(1, R):
            for j in range(1, C):
                if not matrix[i][0] or not matrix[0][j]:
                    # if there is a zero in either row or col, set the row/col to zero
                    matrix[i][j] = 0

        # see if the first row needs to be set to zero as well
        if matrix[0][0] == 0:
            for j in range(C):
                matrix[0][j] = 0

        # see if the first col needs to be set to zero as well
        if is_col_zero:
            for i in range(R):
                matrix[i][0] = 0


# time complexity: O(m x n), where m and n are the number of rows and cols respectively
# space complexity: O(1), in place changes were made, no new matrixes created
