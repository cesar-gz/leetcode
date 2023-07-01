"""
18. 4Sum
Given an array nums of n integers,
return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.
"""

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # to eliminate duplicates
        nums.sort()

        result, quad = [], []       # quad = quadruplet

        # k is how many values we are looking for, starting index, target value
        def kSum(k, start, target):
            if k != 2:
                for i in range(start, len(nums) - k + 1):
                    if i > start and nums[i] == nums[i-1]:
                        continue
                    quad.append(nums[i])
                    kSum(k - 1, i + 1, target - nums[i])
                    quad.pop()
                return

            # base case, 2Sum
            leftPtr, rightPtr = start, len(nums) - 1
            while leftPtr < rightPtr:
                if nums[leftPtr] + nums[rightPtr] < target:
                    # if current sum is less than target
                    leftPtr += 1
                elif nums[leftPtr] + nums[rightPtr] > target:
                    rightPtr -= 1
                else:
                    # we found the target sum
                    result.append(quad + [nums[leftPtr], nums[rightPtr]])
                    leftPtr += 1
                    while leftPtr < rightPtr and nums[leftPtr] == nums[leftPtr - 1]:
                        leftPtr += 1

        kSum(4, 0, target)
        return result
