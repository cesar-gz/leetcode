"""
98. Validate Binary Search Tree

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

node.left < node.val < node.right

Both the left and right subtrees must also be binary search trees.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # where left boundary starts at -infinity, and right boundary starts at +infinity
        def isValid(node, left, right):
            # base case, a empty tree is still a BST
            if not node:
                return True

            # check to see if current value is within correct boundaries
            if not (node.val < right and node.val > left):
                return False

            # check left child first, then right child
            return (isValid(node.left, left, node.val) and
                    isValid(node.right, node.val, right))

        return isValid(root, float("-inf"), float("inf"))
