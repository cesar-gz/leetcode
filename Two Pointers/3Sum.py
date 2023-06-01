"""
15. 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()       # sort ahead of time to make it easier input, O(n log n)

        for index, value in enumerate(nums):
            if index > 0 and value == nums[index-1]:
                continue  # we have the same value as before, skip it to save time

            left, right = index + 1, len(nums)-1    # create two pointers, as in the similar TwoSum problem

            while left < right:
                threeSum = value + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1          # shift our right pointer if the sum is larger than 0
                elif threeSum < 0:
                    left += 1           # shift our left pointer if the sum is smaller than 0
                else:
                    # if we do have it equal 0, we found a triplet that works
                    result.append([value, nums[left], nums[right]])
                    left += 1           # if we also shift the right pointer we will end up missing possible triplets

                    while nums[left] == nums[left-1] and left < right:
                        left += 1       # keep shifting we have the same value, so to save more time from double work

        return result
