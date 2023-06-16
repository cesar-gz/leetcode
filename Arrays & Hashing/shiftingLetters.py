"""
848. Shifting Letters

You are given a string s of lowercase English letters and an integer array shifts of the same length.

Call the shift() of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a').

For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.
Now for each shifts[i] = x, we want to shift the first i + 1 letters of s, x times.

Return the final string after all such shifts to s are applied.
"""

class Solution:
    def shiftingLetters(self, s: str, shifts: list[int]) -> str:
        result = ""

        # both lengths are equal
        length = len(shifts)

        # temp var to store previous value to get sum for left chars
        temp = 0

        # reverse loop to shift right most char 1st, then sum shift of left chars one by one
        for i in range(length-1, -1, -1):
            shift = temp + shifts[i]
            temp = shift
            if shift > 26:
                shift = shift % 26
            result = self.getShiftedChar(ord(s[i]), shift) + result

        return result

    def getShiftedChar(self, char: int, shift: int) -> str:
        asc = char
        asc += shift

        # until this ascii value is within required range
        while asc > 122:
            diff = asc - 122
            asc = 96 + diff
        char = chr(asc)
        return char
