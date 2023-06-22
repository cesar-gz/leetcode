"""
621. Task Scheduler
Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task.
Tasks could be done in any order.
Each task is done in one unit of time.
For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks
(the same letter in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks
"""

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        # count each occurrence of each char in the list
        charCount = Counter(tasks)

        # use negative count to reverse the minHeap into a maxHeap
        maxHeap = [-count for count in charCount.values()]
        heapq.heapify(maxHeap)

        unitsOfTime = 0
        # pairs of [-count, idleTime]
        q = deque()

        # while either maxHeap or queue is not empty
        while maxHeap or q:
            unitsOfTime += 1

            if maxHeap:
                # if maxHeap is not empty, pop from it, add 1 unit of time
                count = heapq.heappop(maxHeap) + 1
                if count:
                    # if count is non zero, add the character count with the (unit of time + idle time)
                    q.append([count, unitsOfTime + n])
            if q and q[0][1] == unitsOfTime:
                # if q is not empty, and the first value in our queue at index 0 is equal to the current time
                heapq.heappush(maxHeap,q.popleft()[0] )

        return unitsOfTime
