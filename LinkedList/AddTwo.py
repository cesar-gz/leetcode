"""
2. Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        current = result

        carry = 0
        while l1 or l2 or carry:
            value1 = l1.val if l1 is not None else 0
            value2 = l2.val if l2 is not None else 0

            value = value1 + value2 + carry
            carry = value // 10
            value = value %10
            current.next = ListNode(value)

            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return result.next
"""
        result = ListNode()

        if l1.val == 0 and l2.val == 0:
            current = result
            current.next = ListNode(0)
            return result.next

        x = 0

        while l1 is not None:
            x = x * 10 + l1.val
            l1 = l1.next

        y = 0

        while l2 is not None:
            y = y * 10 + l2.val
            l2 = l2.next

        z = x + y

        zString = str(z)
        zStringReversed = zString[::-1]

        current = result

        for i in range( len(zStringReversed) ):
            current.next = ListNode( int(zStringReversed[i]) )
            current = current.next

        return result.next

"""
