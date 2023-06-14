"""
24. Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head.
You must solve the problem without modifying the values in the list's nodes
(i.e., only nodes themselves may be changed.)
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def swap_node(node1, node2):
            subsequent_nodes = node2.next
            node2.next = node1
            node1.next = subsequent_nodes
            return node2, node1

        # less than two nodes, return as it is. if head is empty or the node next to head dne
        if not head or not head.next:
            return head

        # take first two nodes as current and current_next
        current, current_next = head, head.next
        resulting_head = None
        previous = None
        # while we have two nodes
        while current and current_next:
            #swap current and current_next
            current, current_next = swap_node(current,current_next)
            if previous:
                # set next of previous to current
                previous.next = current
            if resulting_head is None:
                # set resulting head if its unset
                resulting_head = current
            # set new current, and current_next
            new_current, new_current_next = current_next.next, None
            if new_current:
                new_current_next = new_current.next
            previous = current_next
            current, current_next = new_current, new_current_next
        return resulting_head


# Time Complexity: O(N) as we used a single pass through linked list
# space complexity: O(1) as only use 1 temp node created for any size list
