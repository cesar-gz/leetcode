"""
32. Longest Valid Parentheses

Given a string containing just the characters '(' and ')',
return the length of the longest valid (well-formed) parentheses substring
.
"""

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1] # store -1 for edge cases
        output = 0

        # i is index, p is the character
        for i, p in enumerate(s):
            if p == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    output = max(output, i - stack[-1])

        return output
    # O(N) space, O(1) time
