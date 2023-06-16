"""
445. Add Two Numbers II

You are given two non-empty linked lists representing two non-negative integers.
The most significant digit comes first and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1, stack2 = [], []

        while l1:
            stack1.append(l1.val)
            l1 = l1.next

        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        nextNode, remainder = None, 0

        while stack1 or stack2 or remainder:
            # if stack1 still has nodes to go through, add the value, otherwise initialize to 0
            value1 = stack1.pop() if stack1 else 0
            value2 = stack2.pop() if stack2 else 0
            # dividend = v1 + v2 + remainder, divisor = 10. divmod returns a tuple of the quotient and remainder
            remainder, totalValue = divmod(value1 + value2 + remainder, 10)
            node = ListNode(totalValue, nextNode)
            nextNode = node

        return nextNode
