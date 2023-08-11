"""
647. Palindromic Substrings

Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        output = 0 # the count of palindromic substrs

        for i in range(len(s)):
            # get the odd length palindromes
            l = r = i # set left and right pointers to char at i
            output += self.countPalindromes(s, l, r)

            l = i
            r = i + 1
            # now get the even length palindromes
            output += self.countPalindromes(s, l, r)

        return output

    def countPalindromes(self, s, l, r):
        output = 0  # the count of palindromic substrs
        while l >= 0 and r < len(s) and s[l] == s[r]:
            # we found a palindrome
            output += 1
            l -= 1
            r += 1
        return output
