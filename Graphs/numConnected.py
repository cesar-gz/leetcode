"""
Number of Connected Components in undirected graph

You have a graph of n nodes.
You are given an integer n and an array edges where edges[i] = [ai, bi]
indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.
"""
"""
P -
    1) build the undirected graph
    2) loop over the nodes and run a BFS on the node if it hasn't been visited before.
    3) to optimize the algo, use a global visited set

"""

class Solution:
    def countComponents(self, n:int, edges:List[List[int]]) -> int:
        # create a adjacency list
        adjList = [[] for _ in range(n)]
        for node1, node2 in edges:
            adjList[node1].append(node2)
            adjList[node2].append(node1)

        count = 0

        # keep track of visited nodes in set
        seen = set()
        q = collections.deque()

        for i in range(n):
            if i not in seen:
                q.append(i)
                seen.add(i)
                count += 1
                self.bfs(adjList, q, seen)

        return count

    def bfs(self, adjList, queue, seen):
        while queue:
            node = queue.popleft()
            for neighbor in adjList[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)

    # Time and Space both O(E + V) where e is the edges traversed, and v is the nodes traversed/added to set and queue
