"""
508. Most Frequent Subtree Sum

Given the root of a binary tree, return the most frequent subtree sum.

If there is a tie, return all the values with the highest frequency in any order.

The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself).
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict

class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        # create a hashMap that counts frequencies of a sum
        # a defaultdict allows python to update the value of a key that DNE in the dict
        freqOfSums = defaultdict(int)

        def visit(node):
            # if it is a null node
            if not node:
                return 0

            # calculate subtree sum
            subTreeSum = visit(node.left) + visit(node.right) + node.val

            # increment the freq of this sum in the hashmap
            freqOfSums[subTreeSum] += 1

            # return computed subTreeSum to parent node
            return subTreeSum

        visit(root)

        # create output array
        mostFrequent = []

        highestFreq = 0

        for Sum in freqOfSums:
            # if there are no sums processed yet, just initialize the most freq sum to be the first sum processed
            if len(mostFrequent) == 0:
                mostFrequent.append(Sum)
                highestFreq = freqOfSums[Sum]

            # if we come across a sum whose frequency is equal to the highest freq so far, add it to the result
            elif freqOfSums[Sum] == highestFreq:
                mostFrequent.append(Sum)

            # if we have a sum that is higher then the highest freq so far, remove current sums, update new sum and highest freq
            elif freqOfSums[Sum] > highestFreq:
                mostFrequent = [Sum]
                highestFreq = freqOfSums[Sum]

        return mostFrequent
    # time O(N) because we go through every node
    # space O(N) because we create a hashmap containing each node's sum
