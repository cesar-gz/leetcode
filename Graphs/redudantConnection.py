"""
684. Redundant Connection

In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n,
with one additional edge added.
The added edge has two different vertices chosen from 1 to n,
and was not an edge that already existed.
The graph is represented as an array edges of length n where edges[i] = [ai, bi]
indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes.
If there are multiple answers, return the answer that occurs last in the input.
"""

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # create parent array
        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(n):
            #find its root parent
            p = par[n]

            while p != par[p]:
                # path compression
                par[p] = par[par[p]]
                p = par[p]
            return p

        def Union(node1, node2):
            parent1, parent2 = find(node1), find(node2)

            if parent1 == parent2:
                # already merged
                return False

            if rank[parent1] > rank[parent2]:
                par[parent2] = parent1
                rank[parent1] += rank[parent2]
            else:
                par[parent1] = parent2
                rank[parent2] += rank[parent1]
            return True

        for node1, node2 in edges:
            if not Union(node1, node2):
                return [node1, node2]
