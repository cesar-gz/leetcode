"""
10. Regular Expression Matching

Given an input string s and a pattern p,
implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # top down memoization

        cache = {}

        def DFS(i, j):
            if (i, j) in cache:
                return cache[ (i,j) ]

            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False  # we have some string in s we haven't matched

            match = i < len(s) and (s[i] == p[j] or p[j] == ".")

            if (j+1) < len(p) and p[j+1] == "*":
                # choice 1: dont use the *, or choice 2: use the *
                cache[ (i,j) ] = DFS(i, j + 2) or ( match and DFS(i + 1, j) )
                return cache[ (i,j) ]

            if match:
                cache[ (i,j) ] = DFS(i + 1, j + 1)
                return cache[(i,j)]

            cache[((i,j))] = False
            return False

        return DFS(0, 0)
