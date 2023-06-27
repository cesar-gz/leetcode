"""
239. Sliding Window Maximum
You are given an array of integers nums,
there is a sliding window of size k which is moving from the very left of the array to the very right.
You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.
"""

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # monotonically decreasing queue
        # use a deque to insert and delete at O(1) time

        result = []
        leftPtr = rightPtr = 0
        queue = collections.deque() # going to hold indexes

        # while we are in bounds of array
        while rightPtr < len(nums):
            # while we have a queue, and the right most value in our queue is less than the value we are inserting
            while queue and nums[queue[-1]] < nums[rightPtr]:
                queue.pop()

            queue.append(rightPtr)

            # if the left value is out of bounds
            # remove the left value from the window
            if leftPtr > queue[0]:
                queue.popleft()

            # edge case when left and right == 0
            if (rightPtr + 1) >= k:
                result.append(nums[queue[0]])
                leftPtr +=1

            rightPtr += 1

        return result
