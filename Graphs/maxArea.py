"""
695. Max Area of an Island

You are given an m x n binary matrix grid.
An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical).
You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.
"""

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def helper(i, j):
            # base case: out of bounds, or grid value is 0, return 0
            if i < 0 or i > len(grid) - 1 or j < 0 or j > len(grid[0]) - 1 or grid[i][j] == 0:
                return 0

            # change the grid value to 0 to mark it as visited
            grid[i][j] = 0

            # recursively check 4 neighbors from the current cell for more island cells and add 1 to account for this square
            return helper(i+1, j) + helper(i-1, j) + helper(i, j + 1) + helper(i, j - 1) + 1

        maxArea = 0

        # iterate over the grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # if there is a 1, explore this island with depth first search, and check size against current maxArea
                if grid[i][j] == 1:
                    maxArea = max(maxArea, helper(i,j))

        return maxArea
    # O(N * M) time to view each item in grid
    # O(1) space for the maxArea variable, but O(M*N) for recursive call stack if depth first search goes through entire grid
