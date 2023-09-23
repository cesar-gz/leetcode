"""
743. Network Delay Time

You are given a network of n nodes, labeled from 1 to n.
You are also given times, a list of travel times as directed edges
times[i] = (ui, vi, wi), where ui is the source node,
vi is the target node, and wi is the time it takes
for a signal to travel from source to target.

We will send a signal from a given node k.
Return the minimum time it takes for all the n nodes to receive the signal.
If it is impossible for all the n nodes to receive the signal, return -1.
"""

# Dijkstra's solution
class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        # create a adjacency list that stores the edges
        edges = collections.defaultdict(list)

        for u, v, w in times:
            # add to the source node, the neighbor node and its weight
            edges[u].append((v,w))

        # initialized to the weight of 0, and the starting node k
        minHeap = [(0,k)]
        visited = set()
        # result tracks the minimum time
        result = 0

        while minHeap:
            weight, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)
            result = max(result, weight)

            # do a BFS
            for neighbor, neiWeight in edges[node]:
                if neighbor not in visited:
                    heapq.heappush(minHeap, (weight + neiWeight, neighbor))
        return result if len(visited) == n else -1
