"""
312. Balloon Burst

You are given n balloons, indexed from 0 to n - 1.
Each balloon is painted with a number on it represented
by an array nums. You are asked to burst all the balloons.

If you burst the ith balloon, you will get
nums[i - 1] * nums[i] * nums[i + 1] coins.
If i - 1 or i + 1 goes out of bounds of the array,
then treat it as if there is a balloon with a 1 painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.
"""

class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        # update the nums array, create a cache
        nums = [1] + nums + [1]
        dp = {}

        # takes two indices for the left and right boundaries of a ballon
        def DFS(l, r):
            if l > r:
                # we ran out of balloons to pop
                return 0
            if (l,r) in dp:
                return dp[(l,r)]

            dp[(l,r)] = 0
            for i in range(l, r+1):
                coins = nums[l - 1] * nums[i] * nums[r+1]
                coins += DFS(l, i -1) + DFS(i + 1, r)
                dp[(l,r)] = max(dp[(l,r)], coins)

            return dp[(l,r)]

        return DFS(1, len(nums)-2)
