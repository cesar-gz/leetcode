"""
778. Swim in Rising Water

You are given an n x n integer matrix grid where each value grid[i][j]
represents the elevation at that point (i, j).

The rain starts to fall. At time t, the depth of the water everywhere is t.
You can swim from a square to another 4-directionally adjacent square if
and only if the elevation of both squares individually are at most t.
You can swim infinite distances in zero time.
Of course, you must stay within the boundaries of the grid during your swim.

Return the least time until you can reach the bottom right square
(n - 1, n - 1) if you start at the top left square (0, 0).
"""

# solution with Dijkstra's algo
class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        N = len(grid)
        visited = set()
        minHeap = [ [grid[0][0],0,0] ] # (max(currentTime, prevMaxTime), row, col)
        visited.add( (0,0) )
        directions = [ [0,1], [0,-1], [1,0], [-1,0]]

        while minHeap:
            time, r, c = heapq.heappop(minHeap)

            if r == N - 1 and c == N - 1:
                return time

            # for every difference in row and col
            for dr, dc in directions:
                # find neighboring row and cols
                neiRow, neiCol =  r + dr, c + dc
                # check if we are in bounds of grid
                if (neiRow < 0 or neiCol < 0 or
                    neiRow == N or neiCol == N or
                    (neiRow,neiCol) in visited):
                    continue
                visited.add( (neiRow, neiCol))
                heapq.heappush(minHeap, [max(time, grid[neiRow][neiCol]), neiRow, neiCol])
