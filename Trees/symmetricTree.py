"""
101. Symmetric Tree

Given the root of a binary tree,
check whether it is a mirror of itself (i.e., symmetric around its center).
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def depthFS(leftRoot, rightRoot):
            # base case
            if not leftRoot and not rightRoot:
                # if both left and right roots are null, then they are symmetrical
                return True
            if not leftRoot or not rightRoot:
                # if one of the roots are not null, then they are not symmetrical
                return False

            # now both roots are not null, compare the symmetrical sides with recursion

            return (leftRoot.val == rightRoot.val and
                    depthFS(leftRoot.left, rightRoot.right) and
                    depthFS(leftRoot.right, rightRoot.left))
            # if first condition is False then other functions wont be called, saving time

        return depthFS(root.left, root.right)
        # O(N) time, O(h) space
