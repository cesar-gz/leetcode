"""
25. Reverse Nodes in k-Group

Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list.
If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # two dummy nodes
        tempNode = ListNode(0, head)
        groupPrev = tempNode

        while True:
            kth = self.getKth(groupPrev, k)
            # if null
            if not kth:
                break

            # save pointer
            groupNext = kth.next

            # reverse the current group
            previous, current = kth.next, groupPrev.next
            while current != groupNext:
                temp = current.next
                current.next = previous
                previous = current
                current = temp

            # store the first node in the group
            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp

        return tempNode.next

    def getKth(self, current, k):
        # while were not at the end of the list
        while current and k > 0:
            current = current.next
            k -= 1
        return current
