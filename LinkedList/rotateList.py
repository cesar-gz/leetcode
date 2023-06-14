"""
61. Rotate List
Given the head of a linked list, rotate the list to the right by k places.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            # if the head is empty or k=0
            return head

        # Compute the length of the list
        list_len = 1
        tempNode = head
        while tempNode.next:
            list_len += 1
            tempNode = tempNode.next

        # make the list circular
        tempNode.next = head

        # calculate new rotate size
        k = k % list_len
        new_end = head
        for elem in range(list_len - k - 1):
            new_end = new_end.next
        # make the list linear
        new_start = new_end.next
        new_end.next = None
        return new_start

    # Time complx = O(N), where N is a number of elements in the list
    # space complexity = O(1), since its a constant space solution
