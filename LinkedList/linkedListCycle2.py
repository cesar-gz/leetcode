"""
142. Linked List Cycle II

Given the head of a linked list, return the node where the cycle begins.
If there is no cycle, return null.

Do not modify the linked list.
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        O(N) memory solution:

        current = head
        # keep track of each node in a set
        lookup = set()

        while current:
            if current in lookup:
                return current
            else:
                lookup.add(current)
                current = current.next

        return None
        """

        # edge case
        if not head: return None

        # using floyd's algo
        slowPtr, fastPtr = head, head

        # while we have two nodes ahead of the linked list to iterate through
        while fastPtr.next and fastPtr.next.next:
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next

            if fastPtr == slowPtr:
                break

        if not fastPtr.next or not fastPtr.next.next:
            # there is no cycle
            return None

        slowPtr2 = head

        while slowPtr.next:
            if slowPtr == slowPtr2:
                return slowPtr
            slowPtr = slowPtr.next
            slowPtr2 = slowPtr2.next

        return
