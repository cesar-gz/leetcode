"""
115. Distinct Subsequences

Given two strings s and t, return the number of 
distinct subsequences of s which equals t.

"""
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}
        
        # i is the pointer of str s, j is the pointer of str s
        def DFS(i,j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if(i,j) in dp:
                return dp[(i,j)]
            
            if s[i] == t[j]:
                dp[(i,j)] = DFS(i+1, j+1) + DFS(i+1, j)
            else:
                dp[(i,j)] = DFS(i+1, j)
            
            return dp[(i,j)]
        
        return DFS(0,0)
    # O(n*m) Time and space for n being the length of str s,
    # and m for being the length of str t