"""
210. Course Schedule II

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates
that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses.
If there are many valid answers, return any of them.
If it is impossible to finish all courses, return an empty array.
"""

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # build adjacency list of prereqs
        prereq = { c:[] for c in range(numCourses) }
        for course, preq in prerequisites:
            prereq[course].append(preq)

        # a course has 3 possible states:
        # visited -> course has been added to output
        # visiting -> course has not been added to output, but added to cycle
        # unvisited -> course not added to output or cycle

        output = []
        visit, cycle = set(), set()

        def DFS(course):
            if course in cycle:
                return False
            if course in visit:
                return True
            cycle.add(course)
            for preq in prereq[course]:
                if DFS(preq) == False:
                    return False
            cycle.remove(course)
            visit.add(course)
            output.append(course)
            return True

        for course in range(numCourses):
            if DFS(course) == False:
                # we detected a cycle, we are forced to return empty list
                return []

        return output
