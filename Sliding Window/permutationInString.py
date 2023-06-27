"""
567. Permutation in String

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # if s1 string is longer then s2 string: edge case
        if len(s1) > len(s2):
            return False

        # if we have the 26 "matches" later then we hit the magic number 26 and return true
        s1Count, s2Count = [0] * 26, [0] * 26

        for i in range(len(s1)):
            # get the ASCI value of the char "i" and add it to the array
            s1Count[ord(s1[i]) - ord('a')] += 1 # this will map to one of the 26 indexes for the alphabet
            s2Count[ord(s2[i]) - ord('a')] += 1

        matches = 0

        for i in range(26):
            # if a char exists that is both in s1 and s2, increment matches, if not then add 0
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        # sliding window portion
        leftPtr = 0
        # start at the length of s1, stop when done with s2
        for rightPtr in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[rightPtr]) - ord('a') # to get the index of count arrays
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            # re-do to adjust the right portion of the sliding window
            index = ord(s2[leftPtr]) - ord('a') # to get the index of count arrays
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1

            leftPtr += 1

        if matches == 26: return True
        else: return False
