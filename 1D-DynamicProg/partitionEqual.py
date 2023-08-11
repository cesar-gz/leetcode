"""
416. Partition Equal Subset Sum

Given an integer array nums, return true if you can partition the array into two subsets
such that the sum of the elements in both subsets is equal or false otherwise.
"""

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            # if the sum of the input array is 1(odd), then impossible to get two subsets
            return False

        dp = set()
        dp.add(0) # add the base case of 0
        target = sum(nums) // 2

        for i in range(len(nums) -1, -1, -1): # iterate through nums in reverse
            newDP = set()
            for t in dp:
                if (t + nums[i]) == target:
                    return True
                newDP.add(t + nums[i])
                newDP.add(t)
            dp = newDP

        return True if target in dp else False
    # O(n * sum(nums)) Time
    # O(n) Space for the dp set
