"""
853. Car Fleet
There are n cars going to the same destination along a one-land road. The destination is target miles away.
You are given two integer array position and speed, both of length n, where position[i] is the position of the
ith car and speed[i] is the speed of the ith car(in mph)

A Car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper at the same speed.
The faster car will slow down to match the slower car's speed. The distance between these two cars is ignored.

A car fleet is some non-empty set of cars driving at the same position and same speed. Note that a single car is
also a car fleet. Return the number of car fleets that will arrive at the destination
"""


class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]                              # create an array of pairs, p = position, s = speed

        stack = []                                                                    # will tell us how many car fleets we have in the end

        for p, s in sorted(pair)[::-1]:                                               # sort the array, then iterate in reverse order, from right to left
            stack.append((target - p) / s)                                            # get the speed of the car using decimal division
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                # if there is a car fleet collision between the car in front and car behind it
                stack.pop()   # pop the car behind it, and this way we have one car fleet if a collision did happen

        return len(stack)
