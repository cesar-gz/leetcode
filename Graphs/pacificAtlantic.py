"""
417. Pacific Atlantic Water Flow

There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean.
The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells.
You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells
directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height.
Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

"""

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        pacific, atlantic = set(), set()

        def DFS(r, c, visitedOcean, prevHeight):
            if ( (r,c) in visitedOcean or
                  r < 0 or r == rows or c < 0 or c == cols or
                  heights[r][c] < prevHeight):
                return
            # if were here, then add the new coordinates
            visitedOcean.add( (r,c) )
            # travel the four directions from the coordinates
            DFS(r + 1, c, visitedOcean, heights[r][c])
            DFS(r - 1, c, visitedOcean, heights[r][c])
            DFS(r, c + 1, visitedOcean, heights[r][c])
            DFS(r, c - 1, visitedOcean, heights[r][c])


        for c in range(cols):
            # start by searching the first top row and see what heights can reach downwards toward the atlantic
            DFS(0, c, pacific, heights[0][c])
            # and vice versa, search the bottom row and see what heights can reach upwards toward the pacific
            DFS(rows - 1, c, atlantic, heights[rows - 1][c])

        for r in range(rows):
            # start by search the left col and see what heights can reach westward toward the pacific
            DFS(r, 0, pacific, heights[r][0])
            # and vice versa, search the most right col, and see what heights can reach east ward toward the atlantic
            DFS(r, cols - 1, atlantic, heights[r][cols - 1])

        output = []

        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                     output.append([r,c])

        return output
    # O(M x N) time to traverse each grid cell once, and add to visit sets
    # O(M x N) space to create visited sets
