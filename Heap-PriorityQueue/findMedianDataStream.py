"""
295. Find Median from Data Stream
The median is the middle value in an ordered integer list.
If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
"""

class MedianFinder:
    def __init__(self):
        # two heaps, one minHeap, one maxHeap, where minHeap is smaller than maxHeap
        # heap conditions: equal in size give or take 1. min heap is <= max heap
        self.smallHeap, self.largeHeap= [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.smallHeap, (num) * -1 )      # multiply by -1 to turn it into a maxHeap

        # make sure every num in smallheap is <= num in largeheap
        if self.smallHeap and self.largeHeap and ( self.smallHeap[0] * -1) > self.largeHeap[0]:
            value = heapq.heappop(self.smallHeap) * -1
            heapq.heappush(self.largeHeap, value)

        # if the size difference is uneven, > 1
        if len(self.smallHeap) > len(self.largeHeap) + 1:
            value = heapq.heappop(self.smallHeap) * -1
            heapq.heappush(self.largeHeap, value)
        if len(self.largeHeap) > len(self.smallHeap) + 1:
            value = heapq.heappop(self.largeHeap)
            heapq.heappush(self.smallHeap, value * -1)

    def findMedian(self) -> float:
        if len(self.smallHeap) > len(self.largeHeap):
            return self.smallHeap[0] * -1
        if len(self.largeHeap) > len(self.smallHeap):
            return self.largeHeap[0]

        return ( self.largeHeap[0] + ( self.smallHeap[0] *-1) ) / 2
