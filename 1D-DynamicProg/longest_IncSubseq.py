"""
300. Longest Increasing Subsequence

Given an integer array nums,
return the length of the longest strictly increasing subsequence.
"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums) # cache as long as the input array, each value initialized to 1

        for i in range(len(nums) - 1, -1, -1): # iterate in reverse to save us from doing double work
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)
    # O(n^2) time
    # O(n) space for the dp array of size nums
