"""
973. K Closest Points to Origin

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane
and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)^2 + (y1 - y2)^2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
"""

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        for x, y in points:
            distance = (x ** 2) + (y ** 2)    # dont need to take square root
            minHeap.append([distance, x, y])

        # heapify the list, reorder to have the smallest value at top
        heapq.heapify(minHeap)

        result= []
        while k > 0:
            # keep popping until we get the smallest value
            distance, x, y = heapq.heappop(minHeap)
            result.append([x, y])
            k -= 1

        return result

        # creating a heap O(N) time and space
        # popping from a heap k times is O(k log n) time
