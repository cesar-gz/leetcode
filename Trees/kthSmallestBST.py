"""
230. Kth Smallest element in BST

Given the root of a binary search tree, and an integer k,
return the kth smallest value (1-indexed) of all the values of the nodes in the tree
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # n will tell us the number of elements we visited from the tree
        n = 0

        # instead of recursion, solve iteratively with a stack
        stack = []

        currentNode = root

        # while we have a node and the stack is not empty
        while currentNode and stack:
            while currentNode:
                # go far as left as possible in the tree
                stack.append(currentNode)
                currentNode = currentNode.left
            # we hit the end of the left side, add the last node back
            currentNode = stack.pop()
            n += 1

            if n == k:
                return currentNode.val

            # now check right child as soon as loop starts up again
            currentNode = currentNode.right
