"""
494. Target Sum
You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols
'+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-'
before 1 and concatenate them to build the expression "+2-1".

Return the number of different expressions that you can build,
which evaluates to target.
"""

class Solution:
    # dynamic programming solution
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        dp = {} # Key is (index, total), Value is # of ways

        def backtracking(index, total):
            if index == len(nums):
                return 1 if total == target else 0
            if (index, total) in dp:
                return dp[(index, total)]

            # two decisions, to add the next number or subtract it
            dp[(index, total)] =( backtracking(index + 1, total + nums[index]) +
                                 backtracking(index + 1, total - nums[index]) )
            return dp[(index,total)]

        return backtracking(0,0)
