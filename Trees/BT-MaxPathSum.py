"""
124. Binary Tree Maximum Path Sum

A path in a binary tree is a sequence of nodes where each pair
of adjacent nodes in the sequence has an edge connecting them.
A node can only appear in the sequence at most once.
Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = [root.val]

        # return the max path sum without splitting the subtrees
        def DFS(root):
            if not root:
                return 0

            leftMax = DFS(root.left)
            rightMax = DFS(root.right)

            # incase the numbers are negative
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # compute the max path sum with a split
            result[0] = max(result[0], root.val + leftMax + rightMax)

            return root.val + max(leftMax, rightMax)

        DFS(root)
        return result[0]
