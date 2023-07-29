"""
4. Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively,
return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            #ensuring that A is the smaller of the two
            A, B = B, A

        leftPtr, rightPtr = 0, len(A) - 1
        while True:
            middleA = (leftPtr + rightPtr) // 2
            middleB = half - middleA - 2 # subtract by 2 because of two 1 off errors

            # if middleA DNE, or out of bounds set it neg inf
            Aleft = A[middleA] if middleA >= 0 else float("-infinity")
            Aright = A[middleA + 1] if (middleA + 1) < len(A) else float("infinity")

            Bleft = B[middleB] if middleB >= 0 else float("-infinity")
            Bright = B[middleB + 1] if (middleB + 1) < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                # if here then the partition is correct
                # if middle is odd
                if total % 2:
                    return min(Aright,Bright)
                else:
                    return ( max(Aleft, Bleft) + min(Aright, Bright) ) / 2
            elif Aleft > Bright:
                # Aleft is too big, need to reduce the size of it
                rightPtr = middleA - 1
            else:
                # left partition too small
                leftPtr = middleA + 1
