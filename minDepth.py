"""
111. Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # base case, check if null node, if so return 0
        if not root:
            return 0

        # recursively check the min height from the node

        # case 1: there are two child nodes
        if root.left and root.right:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        # case 2: only one child node
        elif root.right:
            return self.minDepth(root.right) + 1
        elif root.left:
            return self.minDepth(root.left) + 1
        # no nodes, we have leaves
        else:
            return 1

        # O(N) Time we because we need to check every node in the tree
        # O(N) Space for a unbalanced tree with recursion creating stack space
