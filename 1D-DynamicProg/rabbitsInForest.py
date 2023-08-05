"""
781. Rabbits in Forest

There is a forest with an unknown number of rabbits.
We asked n rabbits "How many rabbits have the same color as you?"
and collected the answers in an integer array answers where answers[i]
is the answer of the ith rabbit.

Given the array answers, return the minimum number of rabbits
that could be in the forest.

"""

"""
Plan:

If a rabbit says:
  0: add 1 to our count every time
  1: add 2 to our count every two rabbits
  2: add 3 to our count every three rabbits
  n: add n+1 to our count for every n rabbits
"""

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        currentSum = 0
        totalCounts = {}

        for answer in answers:
            if answer == 0:
                currentSum += 1
            else:
                if answer not in totalCounts or answer == totalCounts[answer]:
                    totalCounts[answer] = 0
                    currentSum += answer + 1
                else:
                    totalCounts[answer] += 1
        return currentSum
