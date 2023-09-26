"""
763 Partition Labels

You are given a string s. We want to partition the string into as many parts
as possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order,
the resultant string should be s.

Return a list of integers representing the size of these parts.
"""

class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        lastIndex = {} # char : last index of it in string s

        # for every index and char in the string, build the hashmap
        for i, c in enumerate(s):
            lastIndex[c] = i

        result = []
        sizeOfPart, endOfPartition = 0, 0
        for i, c in enumerate(s):
            sizeOfPart += 1
            if lastIndex[c] > endOfPartition:
                endOfPartition = lastIndex[c]

            if i == endOfPartition:
                # we are done with the partition
                result.append(sizeOfPart)
                sizeOfPart = 0

        return result
