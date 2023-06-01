"""
167. Two Sum II - Input Array is Sorted

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
find two numbers such that they add up to a specific target number.
Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

You may not use the same element twice.
Your solution must use only constant extra space.

"""

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left, right = 0, len(numbers) - 1     # create two pointers, pointing at opposite ends of the list

        while( left < right ):
            currentSum = numbers[left] + numbers[right]

            if currentSum > target:
                right -= 1                    # move the right pointer to the left
            elif currentSum < target:
                left += 1                     # move the left pointer to the right
            else:
                # we found our two target indices, return them
                return [left + 1, right + 1]  # add plus 1 because we started at 0

        return [] # should not compute if we are given at least one solution
