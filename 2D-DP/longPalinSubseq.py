"""
516. Longest Palindromic Subsequence

Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence
by deleting some or no elements without changing the order of the remaining elements.

"""


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        cache = {}

        def DFS(i, j):
            # base case : going out of bounds with our two pointers
            if i < 0 or j == len(s):
                return 0

            if (i, j) in cache:
                return cache[(i,j)]

            if s[i] == s[j]:
                # the characters match if i and j do not equal each other
                length = 1 if i == j else 2
                cache[(i,j)] = length + DFS(i - 1, j + 1)
            else:
                # the characters do not match
                # try both paths, get the max of the result which would be the longer palindrome
                cache[(i,j)] = max( DFS(i - 1, j), DFS(i, j + 1) )
            return cache[(i,j)]

        for i in range(len(s)):
            DFS(i, i) # calculate the odd length palindromes
            DFS(i, i + 1) # calculate the even length palindromes

        return max(cache.values())
