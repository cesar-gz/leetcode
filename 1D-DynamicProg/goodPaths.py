"""
2421. Number of Good Paths

There is a tree (i.e. a connected, undirected graph with no cycles) consisting of n nodes
numbered from 0 to n - 1 and exactly n - 1 edges.

You are given a 0-indexed integer array vals of length n where vals[i] denotes the value of the ith node.
You are also given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting nodes ai and bi.

A good path is a simple path that satisfies the following conditions:

The starting node and the ending node have the same value.
All nodes between the starting node and the ending node have values less than or equal to the starting node (i.e. the starting node's value should be the maximum value along the path).
Return the number of distinct good paths.

Note that a path and its reverse are counted as the same path. For example, 0 -> 1 is considered to be the same as 1 -> 0.
A single node is also considered as a valid path.
"""

"""
P - 1) Create an adjacency list where adj[X] contains all the neighbors of node X
    2) Create a map valuesToNodes where valuesToNodes[X] is an array that contains all the nodes
          having the value X. The DS chosen will have the keys sorted
    3) Iterate over all the nodes and add each node to valuesToNodes[vals[node]]
    4) Create a class UnionFind defining find and union set
    5) create an instance of unionFind, passing the size as n.
          i) also initialize the count of good paths variable goodPaths with 0
    6) Iterate over each entry value, nodes in valueToNodes in ascending order
          i) for ea node in nodes, for each neighbor of the nodes, we create a map group
          ii) if vals[node] >= vals[neighbor] we perform a union of the node with the neighbor
    7) return good paths

"""

class UnionSet:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.rank = [0 for i in range(n)]

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        xp, yp = self.find(x), self.find(y)

        if xp == yp:
            return
        elif self.rank[xp] == self.rank[yp]:
            self.parents[xp] = yp
            self.rank[yp] += 1
        elif self.rank[xp] < self.rank[yp]:
            self.parents[xp] = yp
        else:
            self.parents[yp] = xp

class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        tree = defaultdict(lambda:set())
        sortedVals = defaultdict(list)
        keys = set()

        for i in range(len(vals)):
            keys.add(vals[i])
            sortedVals[vals[i]].append(i)

        for edge in edges:
            tree[edge[0]].add(edge[1])
            tree[edge[1]].add(edge[0])

        sortedKeys = sorted(list(keys))
        components = UnionSet(len(vals))

        result = 0

        for k in sortedKeys:
            for node in sortedVals[k]:
                for neighbor in tree[node]:
                    if vals[node] >= vals[neighbor]:
                        components.union(neighbor, node)
            babyGraph = defaultdict(int)
            for node in sortedVals[k]:
                babyGraph[components.find(node)] += 1
            for baby, nums in babyGraph.items():
                result += nums * (nums + 1)/2

        return int(result)
    # O(n log n) time to sort
    # O(n) space for every node in the graph
