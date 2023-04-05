"""
739. Daily Temperatures
Given an array of integers, temperatures, return an array, answer, such that answer[i]
is the number of days you have to wait after the ith day to get a warmper temperature.
If there is no future day for which this is possible, keep answer[i] == 0 instead
"""

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        answer = [0] * len(temperatures)        # create our output array with the size of temperatures array
        stack = []                              # every pair is [temperature, index]

        # where i stands for index, t stands for temp
        for i, t in enumerate(temperatures):
            # while the stack is not empty and is the temperature > top of stack
            while stack and t > stack[-1][0]:
                stackTemp, stackIndex = stack.pop()
                answer[stackIndex] = (i - stackIndex)           # this gives us the number of days between n and ith temp
            
            stack.append([t, i])
        return answer