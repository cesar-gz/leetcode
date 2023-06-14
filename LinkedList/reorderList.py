"""
143. Reorder List
You are given the head of a singly linked list. Reorder the list so that the
last node is the second node, and then second node becomes the third node.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find the middle of the linked list
        slowPtr, fastPtr = head, head.next
        # while the faster pointer is not null and hasn't reached the end of the list
        while fastPtr and fastPtr.next:
            # shift pointers
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next

        # save the position in a temp variable
        second = slowPtr.next
        slowPtr.next = None

        previousNode = None
        # while second is not Null, reverse the second portion/half of the input list
        while second:
            tempNode = second.next
            second.next = previousNode
            previousNode = second
            second = tempNode

        # second half is now reversed, merge the two halves of the list
        first, second = head, previousNode
        while second:
            # save
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
