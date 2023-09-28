"""
97. Interleaving Strings

Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where s and t are divided into n and m 
substrings
 respectively, such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.
"""

class Solution:
    # dp solution
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        # create a grid with both axises being the len of each string + 1
        dpGrid = [ [False] * (len(s2)+1) for i in range(len(s1)+1)]

        dpGrid[len(s1)][len(s2)] = True

        # starting in the bottom right, working in reverse to top left
        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                # two decisions if the both chars at our current index are the same char
                if i < len(s1) and s1[i] == s3[i+j] and dpGrid[i + 1][j]:
                    dpGrid[i][j] = True
                if j < len(s2) and s2[j] == s3[i+j] and dpGrid[i][j+1]:
                    dpGrid[i][j] = True

        return dpGrid[0][0]    
        
        
        """
        Recursive solution
        dp = {}

        # our third pointer will be the addition of the two other points
        # k = i + j
        # i tracks the index of s1, j tracks the index of s2, k tracks the index of s3
        def DFS(i,j):
            if i == len(s1) and j == len(s2):
                # out of bounds the problem is done
                return True
            
            if (i,j) in dp:
                return dp[(i,j)]
            
            # two decisions if the both chars at our current index are the same char
            if i < len(s1) and s1[i] == s3[i+j] and DFS(i + 1, j):
                return True
            if j < len(s2) and s2[j] == s3[i+j] and DFS(i, j+1):
                return True
            
            dp[(i,j)] = False
            return False
        
        return DFS(0,0)
        #O(m*n) time, where m is the length of s1, and n is the length of s2
        """