"""
76. Minimum Window Substring

Given two strings s and t of lengths m and n respectively,
return the minimum window substring of s
such that every character in t (including duplicates) is included in the window.

If there is no such substring, return the empty string "".

"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # edge case
        if t == "":
            return ""

        # two hash maps to keep track of the count and help us move through t
        countT, window = {}, {}

        # initialize countT map because it wont change at all
        for char in t:
            countT[char] = 1 + countT.get(char, 0)  # if the char does exist in the hashmap get the value, if not set a default value to 0 and then add 1

        # two variable we create to check if we have the condition of a substr s in t
        have, need = 0, len(countT)

        result, resultLen = [-1, -1], float("infinity")     # initialize to default values

        leftPtr = 0

        for rightPtr in range(len(s)):
            c = s[rightPtr]     # get the char we just reached
            window[c] = 1 + window.get(c, 0)  # add it to the second hash map

            # the first condition
            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                # update our result potentially
                if (rightPtr - leftPtr + 1) < resultLen:    # get the size of the current window
                    result = [leftPtr, rightPtr]
                    resultLen = (rightPtr - leftPtr + 1)

                # pop from the left side of the window
                window[s[leftPtr]] -= 1
                if s[leftPtr] in countT and window[s[leftPtr]] < countT[s[leftPtr]]:
                    have -= 1
                leftPtr += 1

        left, right = result

        if resultLen != float("infinity"):
            # the length changed
            return s[left:right+1]
        else:
            return ""
