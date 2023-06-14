"""
19. Remove Nth Node from End of List

Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # create a node that is pointing to the head
        tempNode = ListNode(0, head)
        leftPtr = tempNode
        rightPtr = head

        # while rightPtr is not Null, shift right until we hit n length
        while n > 0 and rightPtr:
            rightPtr = rightPtr.next
            n -= 1

        # we will slide our two pointers to the right until they are in the right spots
        while rightPtr:
            leftPtr = leftPtr.next
            rightPtr = rightPtr.next

        # delete
        leftPtr.next = leftPtr.next.next
        # return the head, not tempNode
        return tempNode.next
