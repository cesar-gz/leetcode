"""
64. Minimum Path Sum

Given a m x n grid filled with non-negative numbers,
find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
"""


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        # initialize result grid with an extra bottom row and right col
        result = [[float("inf")] * (cols + 1) for r in range(rows + 1)]
        result[rows - 1][cols] = 0

        # iterate in reverse
        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                # get the minimum value of either bottom or right cell
                result[r][c] = grid[r][c] + min(result[r + 1][c], result[r][c + 1])
        return result[0][0]
