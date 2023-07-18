"""
112. Path Sum

Given the root of a binary tree and an integer targetSum,
return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def DFS(node, currSum):
            # in order DFS, takes node and current sum

            # if at a leaf
            if not node:
                return False

            currSum += node.val

            # check if current node has children
            if not node.left and not node.right:
                # if there are no children, check if we hit our target sum
                return currSum == targetSum

            # if there are children nodes
            return ( DFS(node.left, currSum) or DFS(node.right, currSum) )

        return DFS(root, 0)
