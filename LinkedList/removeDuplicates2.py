"""
82. Remove Duplicates from Sorted List II

Given the head of a sorted linked list,
delete all nodes that have duplicate numbers,
leaving only distinct numbers from the original list.

Return the linked list sorted as well.

"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        using more memory solution

        tempList = []
        current = head

        while current:
            tempList.append(current.value)
            current = current.next

        count = Counter(tempList)

        # add every key into the list if the key is not duplicate
        tempList = [key for key, value in count.items() if value == 1]

        dummy = current = ListNode()

        for value in tempList:
            current.next = ListNode(value)
            current = current.next

        return dummy.next
        """
        tempHead = ListNode(0, next = head)

        slowPtr = tempHead

        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                slowPtr.next = head.next
            else:
                slowPtr = slowPtr.next
            head = head.next

        return tempHead.next
