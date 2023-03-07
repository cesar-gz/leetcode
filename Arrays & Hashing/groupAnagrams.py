"""
49. Group Anagrams

Given an array of strings strs, group the anagrams together.
You can return the answer in any order.

"""
import collections

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # create a hashMap that maps the character count (keys) to the list of anagrams (values)
        result = collections.defaultdict(list) # set to default incase an input list is empty

        for string in strs:
            # create an array, initialized to 0, size 26 for the possible alphabet choices
            count = [0] * 26
            for char in string:
                # get the ASCII value of the current char, a = 65, b = 66, ..
                count[ord(char) - ord("a")] += 1
            # group every anagram with this particular count together
            result[tuple(count)].append(string)         #change count to a tuple bc of Python syntax rules

        return result.values()      # O(m * n) where m is the # of input strings, n is the average length of each string
