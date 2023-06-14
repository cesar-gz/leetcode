"""
23. Merge k Sorted Lists

You are given an array of k linked-lists lists,
each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # edge case
        if not lists or len(lists) == 0:
            return None

        # takes pairs of linked lists and merging them each time
        while len(lists) > 1:
            mergedLists = []
            # increment by 2 lists
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                # if there is still another list to make a pair make list2=[i+1], if not list2 = Null
                list2 = lists[i+1] if (i + 1) < len(lists) else None
                # append the merged lists to the merged lists
                mergedLists.append(self.mergeList(list1, list2))
            lists = mergedLists
        return lists[0]


    def mergeList(self, list1, list2):
        tempNode = ListNode()
        tail = tempNode

        # while neither of the two lists are empty
        while list1 and list2:
            # if the value in list 1's node is less than the value in list 2's node
            if list1.val < list2.val:
                # add the list 1's smaller value, then move the list1 to the next node
                tail.next = list1
                list1 = list1.next
            else:
                # add the list2's smaller value, then move the list2 to the next node
                tail.next = list2
                list2 = list2.next
            # move the tail node to the next node
            tail = tail.next
        # if there is still one value left in either list, add it to the end of the tail linked list
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
        return tempNode.next
