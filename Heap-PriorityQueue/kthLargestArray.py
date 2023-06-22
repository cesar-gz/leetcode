"""
215.

Kth Largest Element in an Array

Given an integer array nums and an integer k,
return the kth largest element in the array.

Note that it is the kth largest element in the sorted order,
not the kth distinct element.

You must solve it in O(n) time complexity.

"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # quick sort is O(n^2) but with quick select we can make it to O(n) to look at only a half of n

        # reassign and use k as our index
        k = len(nums) - k

        def quickSelect(leftPtr, rightPtr):
            pivot, pointer = nums[rightPtr], leftPtr

            # create partition
            for i in range(leftPtr, rightPtr):
                if nums[i] <= pivot:
                    # swap nums[i] with index
                    nums[pointer], nums[i] = nums[i], nums[pointer]
                    pointer += 1
            nums[pointer], nums[rightPtr] = pivot, nums[pointer]

            if pointer > k:
                # run quick select now
                return quickSelect(leftPtr, pointer-1)
            elif pointer < k:
                return quickSelect(pointer+1, rightPtr)
            else:
                return nums[pointer]

        return quickSelect(0, len(nums)-1 )
