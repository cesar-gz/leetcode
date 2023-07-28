"""
Connecting Cities with Minimum Cost

There are n cities labeled from 1 to n.
You are given the integer n and an array connections where connections[i] = [xi, yi, costi]
indicates that the cost of connecting city xi and city yi (bidirectional connection) is costi.

Return the minimum cost to connect all the n cities
such that there is at least one path between each pair of cities.
If it is impossible to connect all the n cities, return -1,

The cost is the sum of the connections' costs used.
"""

"""
Plan -
    1) implement the Union Find first as usual with Path Compression using forest
    2) this is a greedy algo, every time you need to find the minimum cost from the
       connections and check if including this edge would cause a loop/cycle, which
       the Union find will help with
    3) Union Find algo helps find the parents of two cities and checks if they
       are not the same, bc if they are then you are already forming a cycle that
       would violate the MST property
    4) append the cost and in the end make these cities a new set using Union
"""

def minimumCost(self, N, connections):
    # traverse all the way to the top root going through parent nodes
    def find(self, parent, i):
      while parent[i] != 1:
          i = parent[i]
      return i

    def Union(self, forest, parent, x, y):
      set1 = self.find(parent, x)
      set2 = self.find(parent, y)

      if set1 != set2:
          if forest[set1] < forest[set2]:
                parent[set1] = set2
                forest[set2] += forest[set1]
          else:
                parent[set2] = set1
                forest[set1] += forest[set2]

      parent = [-1] * (N+1)
      forest = [1] * (N+1)
      self.n = N
      mst = []
      result = 0

      # build graph
      for cityA, cityB, cost in sorted(connections, key = lambda x: x[2]):
          if self.find(parent,cityA) != self.find(parent,cityB):
              mst.append( (cityA, cityB) )
              result += cost
              if len(mst) == N:
                  break
              self.Union(forest, parent, cityA, cityB)
      return result if self.n == 1 else -1
