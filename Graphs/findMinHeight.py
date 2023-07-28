"""
310. Find Minimum Height Tree

A tree is an undirected graph in which any two vertices are connected by exactly one path.
In other words, any connected graph without simple cycles is a tree.

Given a tree of n nodes labelled from 0 to n - 1,
and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree,
you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h.
Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.
"""

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # edge case, if there are only two or less nodes
        if n<=2:
            return [i for i in range(n)]

        # build the graph with the adjacency list
        neighbors = [set() for i in range(n)]
        for start,end in edges:
            neighbors[start].add(end)
            neighbors[end].add(start)

        # initialize the first layer of leaves
        leaves = []
        for i in range(n):
            if len(neighbors[i]) == 1:
                # if that node at neighbors[i] only has one edge
                leaves.append(i)

        # trim the leaves until reaching the centroids
        remainingNodes = n
        while remainingNodes > 2:
            remainingNodes -= len(leaves)
            newLeaves = []
            # remove the current leaves along with the edges
            while leaves:
                leaf = leaves.pop()
                # the only neighbor left for the leaf node
                neighbor = neighbors[leaf].pop()
                # remove the only edge left
                neighbors[neighbor].remove(leaf)
                if len(neighbors[neighbor]) == 1:
                    newLeaves.append(neighbor)
            # prepare the for next round
            leaves = newLeaves
        # the remaining nodes are the centroids of the graph
        return leaves
# O(V) time and space where V is vertices or nodes in the graph
