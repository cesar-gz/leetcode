"""
678. Valid Parenthesis String

Given a string s containing only three types of characters: '(', ')'
and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a
single left parenthesis '(' or an empty string "".
"""

class Solution:
    def checkValidString(self, s: str) -> bool:
        # keep track of  "(" so that we can decide how to handle "*"
        leftMin, leftMax = 0, 0

        for c in s:
            if c == "(":
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif c == ")":
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else:
                # deciding to treat "*' as ")"
                leftMin, leftMax = leftMin - 1, leftMax + 1

            if leftMax < 0:
                return False
            if leftMin < 0:
                leftMin = 0
        # O(1) space, nothing new created
        # O(n) time to process string of length n
        return leftMin == 0
