"""
332. Reconstruct Itinerary

You are given a list of airline tickets where tickets[i] = [fromi, toi] represent
the departure and the arrival airports of one flight.
Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus,
the itinerary must begin with "JFK".
If there are multiple valid itineraries,
you should return the itinerary that has the smallest lexical order
when read as a single string.

For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
You may assume all tickets form at least one valid itinerary.
You must use all the tickets once and only once.

"""

"""
Plan:
  1) sort the tickets
  2) build the graph, assuring all the adjacent nodes are in sorted order
  3) create a current path array to keep track of the path
  4) traverse in DFS from "JFK"
    a) from the current node, visit all adjacent nodes
      i) remove the ticket(edge) from the graph
      ii) traverse the airport (node) to the current path
    b) add the current node to the current path
  5) return the reverse of the current path array

"""

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
      result = []

      graph = collections.defaultdict(list)
      for dest, arrival in tickets:
         # rearrange the destination of the same start together
         graph[dest].append(arrival)

      # get key and value from dictionary, sort the destination
      for dest, arrival in graph.items():
         arrival.sort(reverse=True)

      def DFS(graph, source, result):
         while graph[source]:
            # let the destination empty if we choose it to pop
            newSource = graph[source].pop()
            DFS(graph, newSource, result)
         result.append(source)

      DFS(graph, "JFK", result)
      print(result)
      print(result[::-1])
      return result [::-1]
    # O(NlogN) time where N is the number of tickets sorted
    # O(N) space where N is the total of tickets
