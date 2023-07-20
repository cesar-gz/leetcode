"""
133. Clone Graph
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


P - 0) create a visited dict to save created nodes in memory
    1) define DFS
        - check if node is empty
        - check if node is in cache
        - create new node and save it to map
        - use DFS to copy all neighbors
        - return dfs on given node
    2) run DFS on input


"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = defaultdict(Node)

        def dfs(node: 'Node') -> 'Node':
            if not node:
                return
            elif node in visited:
                return visited[node]
            else:
                # create a new node and save it to the map
                deepCopy = Node(node.val)
                visited[node] = deepCopy
                # use dfs to copy all of its neighbors
                for neighbor in node.neighbors:
                    deepCopy.neighbors.append(dfs(neighbor))
                return deepCopy

        return dfs(node)
    # O(V + E) Time where v is vertexes and e is edges, we need to visit each vertex and edge
    # O(V) Space to hold each node in a hashmap and O(V) again for making a deep copy of all nodes
