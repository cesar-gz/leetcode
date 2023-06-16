"""
658. Find K Closest Elements

Given a sorted integer array arr, two integers k and x,
return the k closest integers to x in the array.
The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
"""

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        leftPtr, rightPtr = 0, len(arr) - k

        # gonna use a binary search to find the target x in the array
        while leftPtr < rightPtr:
            # our midpoint will also server as the left pointer for our sliding window
            midPoint = (leftPtr + rightPtr) // 2
            # arr[midPoint + k] - 1 will be used to check if the right side of the window
            if x - arr[midPoint] > arr[midPoint + k] - x:
                # the value of the right side of the window is closer to the target so
                leftPtr = midPoint + 1
            else:
                # x - arr[midPoint] is closer to the target
                rightPtr = midPoint
        # non inclusive, return the range from the left side of the window up to the k size
        return arr[ leftPtr: leftPtr+k ]
