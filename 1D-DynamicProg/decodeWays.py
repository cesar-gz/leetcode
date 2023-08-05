"""
91. Decode Ways

A message containing letters from A-Z can be encoded into numbers
using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"

To decode an encoded message, all the digits must be grouped then
mapped back into letters using the reverse of the mapping above
(there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)

Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.
"""

class Solution:
    def numDecodings(self, s: str) -> int:

        """
        O(N) space solution with recursion

        dpCache = { len(s) : 1 } # add the first value 1 if the string is just one char

        def DFS(i):
            if i in dpCache:
                return dpCache[i]
            if s[i] == "0": # string is invalid if the first char is 0
                return 0

            output = DFS(i + 1)
            if ( i + 1 < len(s) and (s[i] == "1") or s[i] == "2" and s[i+1] in "0123456"):
                # check if it is in bounds, if the two digits is <= 26
                output += DFS(i + 2)

            dpCache[i] = output
            return output

        return DFS(0)
        """

        dpCache = { len(s) : 1 }

        for i in range(len(s) - 1, -1, -1): # iterate backwards
            if s[i] == "0":
                dpCache[i] = 0
            else:
                dpCache[i] = dpCache[i+1]

            if (i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456")):
                # check if it is in bounds, and if the two digits we are checking are <= 26
                dpCache[i] += dpCache[i+2]

        return dpCache[0]
