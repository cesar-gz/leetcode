"""
232. Implement Queue using Stacks

Implement a first in first out (FIFO) queue using only two stacks.
The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.
Notes:

You must use only standard operations of a stack,
which means only push to top, peek/pop from top, size, and is empty operations are valid.

"""

class MyQueue:

    def __init__(self):
        self.addStack, self.popStack = [], []

    def push(self, x: int) -> None:
        # if we add to the queue, we want to add to the AddStack
        # if we popped, then we want to move all the items from the popStack to the addStack
        while self.popStack:
            self.addStack.append(self.popStack.pop())
        self.addStack.append(x)

    def pop(self) -> int:
        # when we pop from the queue, move items from addStack to popStack
        # this imitates the FIFO policy
        while self.addStack:
            self.popStack.append(self.addStack.pop())
        return self.popStack.pop()

    def peek(self) -> int:
        # if we previously added, look at the last item in the addStack
        # if we previously popped, look at the first item in the popStack
        return self.popStack[-1] if self.popStack else self.addStack[0]

    def empty(self) -> bool:
        # check both stacks to see if they have items
        return True if not self.addStack and not self.popStack else False

    # O(1) Time for all queue operations, O(1) amoritized for pop() and peak()
    # O(N) Space for the total queue spaced used, where n is the amount of elements in the queue
