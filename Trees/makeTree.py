"""
108. Convert Sorted Array into Binary Tree

Given an integer array nums where the elements are sorted in ascending order,
convert it to a height-balanced binary search tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # base case: check for an empty input list, return None if so
        if not nums:
            return None

        # recursively get the index of the root node from the list
        # this will be the element at the center of the input list
        mid = len(nums) // 2
        root = TreeNode(nums[mid])

        # recursively build the left and right subtree by recursively calling
        # the function on each remaining half of the input list
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid +1:])

        return root

    # O(N) time because we go through every element in the input array
    # O(N) space because we need to create N nodes for N input elements
