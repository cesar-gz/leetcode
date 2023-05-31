"""
84. Largest Rectangle in Histogram

Given an array of integers heights representing the histogram's bar height
where the width of each bar is 1, return the area of the largest rectangle in the histogram.

"""


class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        maxArea = 0
        stack = [] # where each pair of elements is (index, height)

        for i, h in enumerate(heights):
            start = i
            # while the stack is not empty and the top of stack's height is greater than the prev height we reached
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index)) # where (i - index is the width)
                start = index # extend the start index backwards
            stack.append((start, h))

        # looking at the entries in our stack that can be left
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i)) # where len(heights) - i is the width

        return maxArea
