"""
Number of People That can be be seen in a Grid

You are given an m x n 0-indexed 2D array of positive integers heights
where heights[i][j] is the height of the person standing at position (i, j).

A person standing at position (row1, col1) can see a person standing at position (row2, col2) if:

The person at (row2, col2) is to the right or below the person at (row1, col1).
More formally, this means that either
row1 == row2 and col1 < col2
or row1 < row2 and col1 == col2.

Everyone in between them is shorter than both of them.
Return an m x n 2D array of integers answer where answer[i][j] is the number of people that the person at position (i, j) can see.
"""

class Solution:
    def seePeople(self, heights: List[List[int]]) -> List[List[int]]:
        # get the length of rows by columns
        m, n = len(heights), len(heights[0])
        # initialize the output array to be the same size of input array
        result = [[0] * n for _ in range(m)]
        # a deque that will act as a mono stkac
        s = collections.deque()

        # looking at the heights to the right
        for i in range(m):
            # iterate in reverse
            for j in range(n - 1, -1, -1):
                number = heights[i][j]
                index = bisect.bisect_left(s, number) # binary search on an increasing order sequence
                # if index is not out of bounds, meaning the next element in 's' is the first one larger than number,
                # we can count it too
                result[i][j] += index + (index < len(s))
                while s and s[0] < number:
                    s.popleft()
                s.appendleft(number)
            s.clear()

        # looking at the heights down below
        for j in range(n):
            for i in range(m - 1, -1, -1):
                number = heights[i][j]
                index = bisect.bisect_left(s, number)
                result[i][j] += index + (index < len(s))
                while s and s[0] < number:
                    s.popleft()
                s.appendleft(number)
            s.clear()

        return result
        # O(m * n) time, O(N) space for the stack used
