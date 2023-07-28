"""
207. Course Schedule

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates
that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create adjacency list that maps each course i, to its prereqs []
        adjList = { i:[] for i in range (numCourses)}
        for course, preReq in prerequisites:
            adjList[course].append(preReq)

        visited = set()

        def DFS(course):
            if course in visited:
                return False
            if adjList[course] == []:
                # if there are no prerequisites
                return True

            visited.add(course)
            for preReq in adjList[course]:
                if not DFS(preReq): return False

            visited.remove(course)
            adjList[course] = []
            return True

        for course in range(numCourses):
            if not DFS(course): return False

        return True
