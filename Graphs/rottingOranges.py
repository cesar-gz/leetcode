"""
994. Rotting Oranges

You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
"""

from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()

        # build the initial set of rotten oranges
        freshOranges = 0
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append( (r,c) )
                elif grid[r][c] == 1:
                    freshOranges += 1

        # create a timestamp and the minutes passed so far
        q.append( (-1,-1) )
        minutes = -1

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        while q:
            row, col = q.popleft()
            if row == -1:
                # we finished one round of processeing
                minutes += 1
                if q:
                    q.append( (-1,-1) ) # to avoid an infinite loop
            else:
                # we have a rotten tomato
                for d in directions:
                    neighborRow, neighborCol = row + d[0], col + d[1]
                    if rows > neighborRow >= 0 and cols > neighborCol >= 0:
                        if grid[neighborRow][neighborCol] == 1:
                            # this fresh orange gets contaminated
                            grid[neighborRow][neighborCol] = 2
                            freshOranges -= 1
                            # this new rotten tomato can contaminate others
                            q.append((neighborRow,neighborCol))
        return minutes if freshOranges == 0 else -1
    # O(N * M) time for the first traversal used to find rotten and fresh oranges, + O(N*M) time for queue traversal
    # O(N * M) space for the queue if all oranges are rotten
