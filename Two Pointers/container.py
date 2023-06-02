"""
11. Container With Most Water

You are given an integer array height of length n.
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container,
such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""

class Solution:
    def maxArea(self, height: list[int]) -> int:
      """
      # method 1 using brute force O(n^2)
      result = 0

      # where left is our left pointer
      for left in range(len(height)):
         for right in range(left + 1, len(height)):
            Area = (right - left) * min(height[left], height[right])      # where left or right doesn't necessarily matter as long as we get the lowest
            result = max(result, Area)

      return result
      """

      # method 2 using linear time
      result = 0
      left, right = 0, len(height)-1  # create two pointers at opposite ends

      while left < right:             # stop when pointers meet each other
         Area = (right - left) * min(height[left], height[right])
         result = max(result, Area)

         # move pointers as necessary
         if height[left] < height[right]:
            left += 1
         else:
            right -= 1

      return result
