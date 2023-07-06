"""
407. Trapping Rain Water 2
Given an m x n integer matrix heightMap
representing the height of each unit cell in a 2D elevation map,
return the volume of water it can trap after raining.
"""

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        # define boundaries
        m,  n = len(heightMap), len(heightMap[0])
        heap = []

        directions = [(-1, 0),(1, 0),(0, -1),(0, 1)]

        for i in range(m):
            for j in range(n):
                # if we are in the first or last column
                if i in {0, m-1} or j in {0, n-1}:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    heightMap[i][j] = -1

        result = 0

        # start with breath first search
        while heap:
            h, i, j = heapq.heappop(heap)

            for dx, dy in directions:
                x = i + dx
                y = j + dy
                if x < 0 or x >= m or y < 0 or y >= n or heightMap[x][y] == -1:
                    continue
                result += max(0, h - heightMap[x][y])

                heapq.heappush(heap, (max(h, heightMap[x][y]), x, y ))
                heightMap[x][y] = -1

        return result
