"""
139. Word Break

Given a string s and a dictionary of strings wordDict,
return true if s can be segmented into a space-separated sequence
of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times
in the segmentation.
"""

"""
Plan (use a DP array to check if any substr from i->j is in the word bank)
1) construct a boolean array of size n+1 as a DP tool
2) set the first index to True
    - this means there is a valid substr up until that index (exclusive)
3) iterate from 0 to N as variable i
    a) if the current index, i, in the DP boolean array is True we iterate from i to N as variable j
      i) if the substr input [i:j] is within the word bank, we mark DP[j] as true
          this signifies the substr of the input from 0 to j is valid
    b) continue to build the solution to the end
4) the boolean value of the last index signifies whether the input str can be broken
"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict) # O(M) space
        dp = [True] + [False] * len(s)
        for i in range(len(s)): # O(N) time
            if dp[i]:
                for j in range(i+1, len(s) + 1): # O(N) time
                    if s[i:j] in wordSet: # O(N) time string generation
                        dp[j] = True

        return dp[-1]
    # O(n^3) time, two nested loops and substr computation at each iteration
    # O(n) space
