"""
22. Generate Parentheses
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        """
        1) only add open parentheses if open ( < n
        2) only add a closing parentheses if closed ) < open
        3) only valid if and only if open == closed == n
        """
        # stack will hold out parentheses and result will be what is returned
        stack = []
        result = []

        # openN is the open count of (, closedN is the closed count of )
        def backTrack(openN, closedN):
            if openN == closedN == n:
                result.append("".join(stack))                 # join every character in the stack together to form a complete string, and append the string
                return                                        # because this is our base case in our recursive solution

            # to add a open parenthesis
            if openN < n:
                stack.append("(")
                backTrack(openN + 1, closedN)                 # when we are done, we will pop the character we just added
                stack.pop()

            # to add a closed parenthesis
            if closedN < openN:
                stack.append(")")
                backTrack(openN, closedN + 1)                 # increment the closedN count
                stack.pop()

        backTrack(0, 0)                                       # finally call the function, with initial values of open and closed count of 0s
        return result
