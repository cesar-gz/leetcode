"""
63. Unique Paths

There is a robot on an m x n grid.
The robot is initially located at the top-left corner (i.e., grid[0][0]).
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).
The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths
that the robot can take to reach the bottom-right corner.

"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}

        def helper(m, n, memo):
            if (m,n) in memo:
                return memo[(m,n)]
            if (n,m) in memo:
                return memo[(n,m)]
            if m == 1 or n == 1:
                return 1
            if m == 0 or n == 0:
                return 0

            # the choice to go down, and the choice to go right
            memo[(m,n)] = helper(m-1, n, memo) + helper(m, n-1, memo)
            return memo[(m,n)]

        return helper(m,n, memo)
