"""
Longest Increasing Path in a Matrix

Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. 
You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).
"""
class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = {} # key: (row,col), value: LIP(Longest Inc Path)

        def DFS(r,c, prev_Val):
            # out of bounds and making sure current val > pre val
            if (r < 0 or r == rows or
                c < 0 or c == cols or
                matrix[r][c] <= prev_Val):
                return 0
            
            if (r,c) in dp:
                return dp[(r,c)]
            
            result = 1 # the minimum a cell can be
            result = max(result, 1 + DFS(r+1,c,matrix[r][c]) )
            result = max(result, 1 + DFS(r-1,c,matrix[r][c]) )
            result = max(result, 1 + DFS(r,c+1,matrix[r][c]) )
            result = max(result, 1 + DFS(r,c-1,matrix[r][c]) )

            dp[(r,c)] = result
            return result
        
        for r in range(rows):
            for c in range(cols):
                DFS(r,c,-1)

        return max(dp.values())
            