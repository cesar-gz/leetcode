"""
846. Hand of Straights

Alice has some number of cards and she wants to rearrange the cards into groups
so that each group is of size groupSize, and consists of groupSize consecutive cards.

Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize,
return true if she can rearrange the cards, or false otherwise.
"""

class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        # check if it is possible to even have a answer
        if len(hand) % groupSize:
            return False

        # create a hash map, of key : count of key
        count = {}
        for val in hand:
            # if the val is in the hashmap, increment it by 1, otherwise set it to 1
            count[val] = 1 + count.get(val , 0)

        # create a minHeap to help maintain a minimum # for a straight hand
        minHeap =  list( count.keys() )
        heapq.heapify(minHeap)

        while minHeap:
            minVal = minHeap[0]

            for i in range(minVal, minVal+groupSize):
                if i not in count:
                    # the value to make a straight is unavailable so return False
                    return False
                # decrement count
                count[i] -= 1
                # pop from the minHeap
                if count[i] == 0:
                    # if we are popping from the minHeap that is not the min val in the minHeap
                    if i != minHeap[0]:
                        # return False because the next grouping will be incorrect
                        return False
                    heapq.heappop(minHeap)
        return True
