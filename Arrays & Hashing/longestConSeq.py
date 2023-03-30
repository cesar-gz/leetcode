"""
128. Longest Consecutive Sequence

Given an unsorted array of integers nums, return the length of the
longest consecutive elements sequence. Must be in O(n) time.

"""

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        setOfNums = set(nums)
        longestCSeq = 0

        for number in nums:
            if (number - 1) not in setOfNums:             # Then we have the start of a sequence
                length = 0
                while (number + length) in setOfNums:
                    length += 1
                longestCSeq = max(length, longestCSeq)

        return longestCSeq
