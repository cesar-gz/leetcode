"""
873. Length of Longest Fibonacci Subsequence

Given a strictly increasing array arr of positive integers forming a sequence,
return the length of the longest Fibonacci-like subsequence of arr. If one does not exist, return 0.

A subsequence is derived from another sequence arr by deleting any number of elements (including none) from arr,
without changing the order of the remaining elements.
For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8].
"""

class Solution:
    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        s = set(arr)
        best = 0

        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                a, b = arr[i], arr[j]
                count = 1

                while b in s:
                    count += 1
                    a, b = b, a + b

                if count >= 3:
                    best = max(best, count)
        return best
