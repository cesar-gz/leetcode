"""
1448. Count Good Nodes in Binary Tree

Given a binary tree root,
a node X in the tree is named good if in the path
from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def DFS(node, currMaxValue):
            if not node:
                return 0

            output = 1 if node.val >= currMaxValue else 0
            currMaxValue = max(currMaxValue, node.val)
            output += DFS(node.left, currMaxValue)
            output += DFS(node.right, currMaxValue)
            return output

        return DFS(root, root.val)
