"""
2367. Number of Arithmetic Triplets

You are given a 0-indexed, strictly increasing integer array nums and a positive integer diff.
A triplet (i, j, k) is an arithmetic triplet if the following conditions are met:

i < j < k,
nums[j] - nums[i] == diff, and
nums[k] - nums[j] == diff.

Return the number of unique arithmetic triplets.
"""

class Solution:
    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:
        # create two dictionaries that map number to count of that number

        # firstNum[x] is the number of the beginning of a triplet starting with x
        firstNum = collections.Counter()
        # secondNum[x] is the number of the middle of a triplet with the middle being x
        secondNum = collections.Counter()

        total = 0

        for x in nums:
            # if x is the last number, how many sequences do we have were x already exists
            total += secondNum[x - diff]

            # where is x in the middle of the triplet if it already exists
            secondNum[x] += firstNum[x - diff]

            # if this is the beginning of the triplet, then this is the number of the count
            firstNum[x] += 1

        return total
