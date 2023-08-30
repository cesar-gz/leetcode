"""
659. Encode and Decode Strings

Design an algorithm to encode a list of strings to a string. The encoded string is then
sent over the network and is decoded back to the original list of strings.
"""
class Solution:
    def encode(self, strs):
        output = ""

        for s in strs:
            # ex: 5#apple
            output += str(len(s)) + "#" + s

        return output

    def decode(self, strs):
        output, i = [], 0

        while i < len(str):
            j = i
            while str[j] != "#":
                j += 1
            length = int(str[i:j]) # this is the integer
            output.append( str[j + 1 : j + 1 + length] ) # this is the string
            i = j + 1 + length # move to the beginning of the next string

        return output
