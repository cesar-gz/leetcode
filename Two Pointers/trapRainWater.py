"""
42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.
"""

class Solution:
    def trap(self, height: list[int]) -> int:
        # if there is no input return 0
        if not height: return 0

        left, right = 0, len(height)-1                      # create two opposite pointers
        leftMax, rightMax = height[left], height[right]     # keep track of possible heights that prevent water from overflowing on either ends
        result = 0                                          # represents our total water trapped

        # before the pointers meet each other
        while left < right:
            if leftMax < rightMax:
                left += 1                                   # move left pointer
                leftMax = max(leftMax, height[left])        # update the leftMax to whatever the highest boundary is
                result += leftMax - height[left]            # trap water and add it to our total

            else:
                # if leftMax > rightMax
                right -= 1
                rightMax = max(rightMax, height[right])
                result += rightMax - height[right]

        return result
