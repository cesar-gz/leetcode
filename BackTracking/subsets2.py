"""
90. Subsets II

Given an integer array nums that may contain duplicates, return all possible subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
"""

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        output = []

        nums.sort()

        def backtrack(index, subset):
            if index == len(nums):
                output.append(subset[::])
                # add a copy when we reach the end of the array
                return

            # all subset that include nums[index]
            subset.append(nums[index])
            backtrack(index + 1, subset)
            subset.pop()

            # all subset that do not include nums[index]
            while index+1 < len(nums) and nums[index] == nums[index+1]:
                # iterate the index so that we are not on a duplicate in the nums array
                index += 1
            backtrack(index+1, subset)

        backtrack(0, [])
        return output
