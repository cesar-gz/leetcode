"""
138. Copy List with Random Pointer

A linked list of length n is given such that each node contains an additional random pointer,
which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes,
where each new node has its value set to the value of its corresponding original node.
Both the next and random pointer of the new nodes should point to new nodes in the copied list
such that the pointers in the original list and copied list represent the same list state.
None of the pointers in the new list should point to nodes in the original list.

Return the head of the copied linked list.

Your code will only be given the head of the original linked list.

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        # map every old node to the copy of the new node, where Null points to Null
        oldToCopy = { None : None}

        # first pass through linked list, mapping and making the copies
        current = head
        while current:
            copy = Node(current.val)
            oldToCopy[current] = copy
            current = current.next

        # second pass, updating pointers to the correct spots
        current = head
        while current:
            copy = oldToCopy[current]
            copy.next = oldToCopy[current.next]
            copy.random = oldToCopy[current.random]
            current = current.next

        return oldToCopy[head]
