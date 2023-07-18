"""
200. Number of Islands

Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water),
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
      if not grid:
         # if the grid is empty
         return 0

      # get the dimensions
      rows, cols = len(grid), len(grid[0])
      # keep a record of 1s from the island
      visited = set()
      islands = 0

      def BFS(row, column):
         q = collections.deque()
         visited.add( (row,column) )
         q.append( (row,column) )

         while q:
            row, col = q.popleft()
            # move to the right, left, above, and below
            directions = [[1,0], [-1,0], [0,1], [0,-1]]

            for dirRow, dirCol in directions:
               r, c = row + dirRow, col + dirCol
               if ( r in range(rows) and
                    c in range(cols) and
                    grid[r][c] == "1" and
                    (r, c) not in visited):
                    q.append( (r, c) )
                    visited.add( (r, c) )

      for row in range(rows):
         for col in range(cols):
            if grid[row][col] == "1" and (row, col) not in visited:
               # we found a new island, use breadth first search
               BFS(row, col)
               islands += 1

      return islands
