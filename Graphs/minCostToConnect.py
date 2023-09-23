"""
1584. You are given an array points representing integer coordinates
of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance
between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected.
All points are connected if there is exactly one simple path between any two points.
"""

class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        N = len(points)

        # i : list of [cost, neighborNode]
        adjList = { i:[] for i in range(N)}
        for i in range(N):
            x1, y1 = points[i]
            # compare point i to every other point
            for j in range(i + 1, N):
                x2, y2 = points[j]
                manhattanDist = abs(x1 - x2) + abs(y1 - y2)
                adjList[i].append([manhattanDist, j])
                adjList[j].append([manhattanDist, i])

        # Prims Algo
        result = 0
        visited = set()
        minHeap = [[0,0]] # each pair is [cost, coordinate point]
        while len(visited) < N:
            cost, point = heapq.heappop(minHeap)
            if point in visited:
                continue
            result += cost
            visited.add(point)
            for neiCost, neighbor in adjList[point]:
                if neighbor not in visited:
                    heapq.heappush(minHeap, [neiCost, neighbor])

        return result
