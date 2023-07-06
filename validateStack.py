"""
946. Validate Stack Sequences

Given two integer arrays pushed and popped each with distinct values,
return true if this could have been the result of a sequence of push and pop operations on an initially empty stack,
or false otherwise.
"""

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        """
        Plan:
        1. use a stack to verify the input
        2. have a pointer index for each array to keep track of our operations
        3. if the current value of pushed != value at popped, push that value
        4. else then pop that value
        5. if after popping, the popped value does not match, then this is an incorrect popped array so return False
        6. after going through the pushed array with no issues then we should check our stack
        7. start popping each elem from the stack and compare it to the remaining values of the popped array
        8. if there are no mismatched results, return True
        """

        j = 0
        stack = []
        for x in pushed:
            stack.append(x)
            while stack and j < len(popped) and stack[-1] == popped[j]:
                stack.pop()
                j += 1

        return j == len(popped)
        # O(N) time and space, where N is the stack space and the length of pushed/popped
