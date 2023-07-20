"""
1615. Maximal Network Rank

There is an infrastructure of n cities with some number of roads connecting these cities.
Each roads[i] = [ai, bi] indicates that there is a bidirectional road between cities ai and bi.

The network rank of two different cities is defined as the total number of directly connected roads to either city.
If a road is directly connected to both cities, it is only counted once.

The maximal network rank of the infrastructure is the maximum network rank of all pairs of different cities.

Given the integer n and the array roads, return the maximal network rank of the entire infrastructure.
"""

"""
P - 1) use a hash table of size n, which stores sets for each city. Members of the sets are cities which are directly connected to the city set correspond to
    2) then examine all unique pairs (city1, city2)
    3) sum up the edges of all cities
    4) if there is an edge between both cities, the sum needs to be reduced by 1 since the edge is counted 2 times
    5) then store the highest sum of edges and return it
"""

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        # use a set to store the neighbors
        cityToCities = [ set() for i in range(n)]

        maxNetworkRank = 0

        # check ea pair of cities , add their ranks together
        # for each (i, j) pair, if i is the neighbor of j or vice versa, decrement the rank

        for road in roads:
            cityToCities[ road[0] ].add( road[1] )
            cityToCities[road[1]].add(road[0])

        for cityA in range(n):
            for cityB in range(cityA + 1, n):
                networkRank = len( cityToCities[cityA] ) + len( cityToCities[cityB] )
                if cityA in cityToCities[cityB]:
                    networkRank -= 1
                maxNetworkRank = max(maxNetworkRank, networkRank)

        return maxNetworkRank
    # O(E + V^2) Time if all nodes have the same amount of edges, where v is the number of cities
    # O(E) space, where E is edges, and where we store each city's neighbor in a hash table
