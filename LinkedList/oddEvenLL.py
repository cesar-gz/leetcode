"""
328. Odd Even Linked List

Given the head of a singly linked list,
group all the nodes with odd indices together
followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups
should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None or head.next.next is None:
            # first three nodes are empty
            return head

        evenHead = head.next
        currentOdd = head
        currentEven= evenHead

        # while there is a list to traverse, not Null
        while currentOdd.next and currentEven.next:
            currentOdd.next = currentOdd.next.next
            currentEven.next = currentEven.next.next
            currentOdd = currentOdd.next
            currentEven = currentEven.next

        currentOdd.next = evenHead
        return head
