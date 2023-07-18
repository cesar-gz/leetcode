"""
515. Find largest value in each tree row

Given the root of a binary tree,
return an array of the largest value in each row of the tree (0-indexed).
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import sys, queue

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            # edge case, there is no nodes
            return []

        output = []
        q = queue.Queue()

        # add the root
        q.put(root)

        while q.qsize() > 0:
            # initialize current max to highest negative value possible
            currMax = -sys.maxsize

            for _ in range(q.qsize()):
                # grab the current node
                node = q.get()
                currMax = max(currMax, node.val)

                # update queue if there are child nodes
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)

            output.append(currMax)

        return output
    # O(N) time since we went through every node
    # O(N) space since we made a queue that held all nodes
