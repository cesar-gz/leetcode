"""
102. Binary Tree Level Order Traversal

Given the root of a binary tree,
return the level order traversal of its nodes' values.
(i.e., from left to right, level by level).
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []

        from collections import deque
        q = collections.deque()
        q.append(root)

        while q:
            length = len(q)
            level = []
            for i in range(length):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
              output.append(level)

        return output
