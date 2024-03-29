"""
45. Jump Game II

You are given a 0-indexed array of integers nums of length n. 
You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward 
jump from index i. In other words, if you are at nums[i], 
you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n

Return the minimum number of jumps to reach nums[n - 1]. 
The test cases are generated such that you can reach nums[n - 1].
"""

# greedy solution with a simple BFS style
class Solution:
    def jump(self, nums: List[int]) -> int:
        result = 0
        leftPtr = rightPtr = 0

        # while right is inside the array
        while(rightPtr < len(nums)-1):
            # see how far we can jump
            farthest = 0

            for i in range(leftPtr, rightPtr + 1):
                # is our current jump bigger than the farthest so far
                farthest = max(farthest, i + nums[i])
            leftPtr = rightPtr + 1
            rightPtr = farthest
            result += 1
        
        return result