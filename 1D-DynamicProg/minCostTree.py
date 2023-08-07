"""
1130. Minimum Cost Tree From Leaf values

Given an array arr of positive integers, consider all binary trees such that:

Each node has either 0 or 2 children;
The values of arr correspond to the values of each leaf in an in-order traversal of the tree.
The value of each non-leaf node is equal to the product of the largest leaf value in its left and right subtree, respectively.
Among all possible binary trees considered, return the smallest possible sum of the values of each non-leaf node.
It is guaranteed this sum fits into a 32-bit integer.

A node is a leaf if and only if it has zero children.
"""

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        output = 0
        while len(arr) > 1:
            index = arr.index(min(arr))
            if 0 < index < len(arr) - 1:  # if the smallest value index is not the first or last element in the arr
                # add to the output the smallest val in the arr * the smallest val next to it
                output += arr[index] * min( arr[index-1], arr[index+1] )
            else:
                # add to the output the val of the first elem in the arr or the last element
                output += arr[index] * ( arr[index+1] if index == 0 else arr[index - 1] )
            arr.pop(index)
        return output
