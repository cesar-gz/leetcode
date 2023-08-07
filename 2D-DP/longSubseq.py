"""
1143. Longest Common Subsequence

Given two strings text1 and text2, return the length of their longest common subsequence.
If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none)
deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # create 2d grid for Dynamic Programming, with an extra botton row and right col
        dp = [ [ 0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        # iterate in reverse
        for i in range(len(text1) -1, -1, -1):
            for j in range(len(text2) -1, -1, -1):
                if text1[i] == text2[j]:
                    # if the characters match each other
                    dp[i][j] = 1 + dp[i+1][j+1] # move diagonal
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i + 1][j]) # characters dont match check the right col's char and bottom col's char

        return dp[0][0] # the top left cell will have the total
    # O(m*n) memory and space for grid, m is length of text 1, n is length of text2
