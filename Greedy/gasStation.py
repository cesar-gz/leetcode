"""
134. Gas Station

There are n gas stations along a circular route,
where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel
from the ith station to its next (i + 1)th station.
You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index
if you can travel around the circuit once in the clockwise direction,
otherwise return -1. If there exists a solution, it is guaranteed to be unique
"""

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        # check if a solution exists
        if sum(gas) < sum(cost):
            return -1

        total = 0
        result = 0 # starting index to start trying

        # start checking every position
        for i in range(len(gas)):
            difference = (gas[i] - cost[i])
            total += difference

            if total < 0:
                # if negative, this position would not allow us to move forward
                total = 0       # reset the total
                result = i + 1  # change the starting position to the next one

        return result
