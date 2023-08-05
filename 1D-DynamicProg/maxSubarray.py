"""
152. Maximum Product Subarray

Given an integer array nums, find a subarray
that has the largest product, and return the product.

"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        output = max(nums) # set output to the max value in nums
        currentMin, currentMax = 1, 1

        for n in nums:
            if n == 0:
                # 0s will mess up min and max
                currentMin, currentMax = 1, 1
                continue

            temp = currentMax * n # save old value
            currentMax = max(n * currentMax, n * currentMin, n)
            currentMin = min(temp, n * currentMin, n)

            output = max(output, currentMax, currentMin)

        return output
