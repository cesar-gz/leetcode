"""
287. Find the Duplicate Num

Given an array of integers nums containing n + 1 integers
where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

"""


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # phase 1, floyds algo, turtle and rabbit
        slowPtr, fastPtr= 0, 0
        while True:
            slowPtr = nums[slowPtr]
            fastPtr = nums[nums[fastPtr]]
            if slowPtr == fastPtr:
                break

        # phase 2
        slowPtr2 = 0
        while True:
            slowPtr = nums[slowPtr]
            slowPtr2 = nums[slowPtr2]
            if slowPtr == slowPtr2:
                return slowPtr
