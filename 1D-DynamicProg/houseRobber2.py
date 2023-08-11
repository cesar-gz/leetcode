"""
213. House Robber II

You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed.
All houses at this place are arranged in a circle.
That means the first house is the neighbor of the last one.
Meanwhile, adjacent houses have a security system connected, and it will automatically
contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting the police.
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        val1 = self.helper(nums[1:])  # pass the entire array skipping the first house
        val2 = self.helper(nums[:-1]) # skip the last house
        mostRobbed = max(nums[0], val1, val2)
        return mostRobbed

    def helper(self, nums):
        rob1, rob2 = 0, 0 # store the max amount you can rob from the prev two houses

        for n in nums:
            # go through every house
            newRob = max(rob1 + n, rob2)
            rob1 = rob2   # update the two new max amounts
            rob2 = newRob

        return rob2
