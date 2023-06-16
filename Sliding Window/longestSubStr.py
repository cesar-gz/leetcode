"""
3. Longest Substring without repeating characters

Given a string s, find the length of the longest substring without repeating characters.

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        setOfChars = set()
        leftPtr = 0
        result = 0

        for rightPtr in range(len(s)):
            while s[rightPtr] in setOfChars:
                # if we have a duplicate character in our input string, remove the duplicate
                setOfChars.remove(s[leftPtr])
                leftPtr += 1
            setOfChars.add(s[rightPtr])
            result = max(result, len(setOfChars) )

        return result
