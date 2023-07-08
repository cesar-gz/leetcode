"""
814. Binary Tree Pruning

Given the root of a binary tree,
return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

A subtree of a node, is node plus every node that is a descendant of node.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def pruneHelper(node):
            # assume that the left subtree does not contain a 1
            leftSubtreeContains1 = False

            # if there is a leaf child, then the left subtree could have a 1, so recursively check this
            if node.left:
                leftSubtreeContains1 = pruneHelper(node.left)

            # assume that the right subtree does not contain a 1
            rightSubtreeContains1 = False

            # if there is a right child, then the right subtree could have a 1, so recursively check this
            if node.right:
                rightSubtreeContains1 = pruneHelper(node.right)

            # if left subtree does not have a 1, remove per problems description
            if not leftSubtreeContains1:
                node.left = None

            # if right subtree does not have a 1, remove per problems description
            if not rightSubtreeContains1:
                node.right = None

            """
              the subtree rooted at this node contains a 1 if:
              1) the root of the subtree has a 1
              2) the left subtree has a 1
              3) the right subtree has a 1
            """

            # the parent node will use this value to determine if there needs a pruning or not
            return node.val == 1 or leftSubtreeContains1 or rightSubtreeContains1

        checkTree = pruneHelper(root)

        # if the tree does not contain a 1, then all nodes (including the root) should be removed
        if not checkTree:
            return None
        else:
            return root

        # O(N) time because we process every node once
        # O(N) space because the recursion call stack can be as tall as the tree
