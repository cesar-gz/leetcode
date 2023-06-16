"""
424. Longest Repeating Character Replacement

You are given a string s and an integer k.
You can choose any character of the string and change it to any other uppercase English character.
You can perform this operation at most k times.

Return the length of the longest substring containing the same letter
you can get after performing the above operations.

"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # starting index for the string, and a hash map that maps chars to their frequencies
        start = 0
        frequencyMap = {}
        maxFreq = 0
        longest_SubStr_length = 0

        for endChar in range(len(s)):
            # if the char is in the map, get it and increment it by 1. If not in there then add it, and initialize it to 1
            frequencyMap[s[endChar]] = frequencyMap.get(s[endChar], 0) + 1

            # the max freq we have seen in any window yet
            maxFreq = max(maxFreq, frequencyMap[s[endChar]])

            # move the start pointer towards the right if the current window is invalid
            isValid = (endChar + 1 - start - maxFreq <= k)
            if not isValid:
                frequencyMap[s[start]] -= 1
                start += 1

            # the window is valid at this point, store the length
            # size of the window never decreases
            longest_SubStr_length = endChar + 1 - start

        return longest_SubStr_length

# Time Complexity O(N) where n is the number of characters in the string
# space complexity O(M) where m represents if there are m unique characters, then the memory required is proportional to m
