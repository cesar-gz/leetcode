"""
Given a binary tree, return the vertical order traversal of its nodes values.

For each node at position (X, Y), its left and right children respectively will be at positions (X-1, Y-1) and (X+1, Y-1).

Return a list of lists of the elements in each vertical level, from left to right and top to bottom in each list.
"""

# Traverse through the tree and keep track of the horizontal distance to the center as we traverse.
# place node values in a HashMap with the key being the horizontal distance to the center

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        nodeList = []

        def DFS(node, row, col):
            if node is None:
                nodeList.append( (col, row, node.val) )
                # preorder DFS, search left child then right child
                DFS(node.left, row + 1, col + 1)
                DFS(node.right, row - 1, col - 1)

        # construct the node list with the coordinates
        DFS(root, 0, 0)

        # sort the node list globally according to coordinates
        nodeList.sort()

        # retrieve the sorted results grouped by col index
        result = []
        currColIndex = nodeList[0][0]
        currCol = []

        for column, row, value in nodeList:
            if column == currColIndex:
                currCol.append(value)
            else:
                # we are at the end of the col, start a new one
                result.append(currCol)
                currColIndex = column
                currCol = [value]
        # add the last col
        result.append(currCol)

        return result
        # O(NlogN) time since we used DFS and sorted the list of elements which is N nodes of input tree
        # O(N) space because we used a queue data structure to maintain the order of visits
