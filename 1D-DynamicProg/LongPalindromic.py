"""
5. Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.

A string is palindromic if it reads the same forward and backward.
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        output = ""
        length = 0

        for char in range(len(s)):
            # check odd length palindromes
            leftPtr, rightPtr = char, char
            while leftPtr >= 0 and rightPtr < len(s) and s[leftPtr] == s[rightPtr]:
                # check to see if its our longest palindrome so far
                if (rightPtr - leftPtr + 1) > length:
                    output = s[leftPtr:rightPtr + 1]
                    length = rightPtr - leftPtr + 1
                leftPtr -= 1
                rightPtr += 1

            # check even length palindromes
            leftPtr, rightPtr = char, char + 1
            while leftPtr >= 0 and rightPtr < len(s) and s[leftPtr] == s[rightPtr]:
                if (rightPtr - leftPtr + 1) > length:
                    output = s[leftPtr:rightPtr + 1]
                    length = rightPtr - leftPtr + 1
                leftPtr -= 1
                rightPtr += 1

        return output
