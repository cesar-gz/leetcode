"""
787. Cheapest Flights Within K Stops

There are n cities connected by some number of flights.
You are given an array flights where flights[i] = [fromi, toi, pricei]
indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k,
return the cheapest price from src to dst with at most k stops.
If there is no such route, return -1.

"""
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # build a adjacency matrix
        adjMat = [[0 for _ in range(n)] for _ in range(n)]
        for s, d, w in flights:
            adjMat[s][d] = w

        # shortest distances array
        distances = [float("inf") for _ in range(n)]
        currentStops = [float("inf") for _ in range(n)]
        distances[src], currentStops[src] = 0, 0

        # data is cost, stops, node
        minHeap = [(0,0, src)]

        while minHeap:
            cost, stops, node = heapq.heappop(minHeap)

            # if the destination is reached
            if node == dst:
                return cost

            # if there are no more stops left, continue
            if stops == k + 1:
                continue

            # examine and relax all neighboring edges if possible
            for neighbor in range(n):
                if adjMat[node][neighbor] > 0:
                    dU, dV, wUV = cost, distances[neighbor], adjMat[node][neighbor]

                    # is there a better cost?
                    if dU + wUV < dV:
                        distances[neighbor] = dU + wUV
                        heapq.heappush(minHeap, (dU + wUV, stops + 1, neighbor))
                        currentStops[neighbor] = stops
                    elif stops < currentStops[neighbor]:
                        # better stops?
                        heapq.heappush(minHeap, (dU + wUV, stops + 1, neighbor))

        return -1 if distances[dst] == float("inf") else distances[dst]
    # O(KE) time where E is # of edges and K is the # of stops
    # O(V) space where V is # of nodes in flights
