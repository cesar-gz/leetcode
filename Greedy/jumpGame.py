"""
55. Jump Game

You are given an integer array nums. 
You are initially positioned at the array's first index, 
and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
"""
# greedy solution
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # set at the end of the input arr
        goalPost = len(nums) - 1

        # iterate in reverse
        for i in range(len(nums)-1, -1, -1):
            # if the jump range is at the goal
            if i+nums[i] >= goalPost:
                # shift goalpost closer to start
                goalPost = i
            
        return True if goalPost == 0 else False