"""
141. Linked List Cycle

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list
that can be reached again by continuously following the next pointer.

Internally, pos is used to denote the index of the node that tail's next pointer is connected to.
Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slowPtr, fastPtr = head, head           # create two pointers like in the tortoise and hare algorithm

        while fastPtr and fastPtr.next:         # if the fast pointer is null then there is no cycle
          slowPtr = slowPtr.next
          fastPtr = fastPtr.next.next           # shift fast pointer by two
          if slowPtr == fastPtr:                # if the fast pointer meets the slow pointer, then there is a cycle
             return True

        return False
