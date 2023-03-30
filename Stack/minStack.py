"""
155. Min Stack
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:
MinStack() initializes the stack object
void push(int val), void pop(), int top(), and int getMin()
retrieves the minimum element in the stack
Must run in O(1) time
"""

class MinStack:
    def __init__(self):
        self.stack = []                                            # our regular stack that we are using for push, pop, and top
        self.minStack = []                                         # a second stack to help us keep track of the current min val at different stack levels

    def push(self, val:int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)     # val with be the minimum of itself or the top of our second stack if its smaller.
                                                                        # if our minStack is empty then use val
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()                                            # using built in functions to save time
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
