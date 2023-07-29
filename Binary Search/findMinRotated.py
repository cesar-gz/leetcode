"""
153. Find Minimum in Rotated Sorted Array

Suppose an array of length n sorted in ascending order is rotated
between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time
results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements,
return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # using an altered binary search algo
        result = nums[0] # set random default value

        leftPtr, rightPtr = 0, len(nums) - 1

        while leftPtr <= rightPtr:
            # if we get to a subarray that is already sorted
            if nums[leftPtr] < nums[rightPtr]:
                result = min(result, nums[leftPtr])
                break
            # if the array is not sorted, start binary search
            mid = (leftPtr + rightPtr) // 2
            result = min(result, nums[mid])

            if nums[mid] >= nums[leftPtr]:
                # then the target is in the right portion of the array, search the right side
                leftPtr = mid + 1
            else:
                # search the left portion
                rightPtr = mid - 1

        return result
