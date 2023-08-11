"""
131. Palindrome Partitioning

Given a string s, partition s such that every substring
of the partition is a palindrome. Return all possible palindrome partitioning of s.

"""

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        output = []
        currentPart = []

        def DFS(index):
            if index >= len(s):
                output.append(currentPart[:]) # add a copy to the return output
                return
            for j in range(index, len(s)):
                # where index is the left boundary, and j is the right boundary
                if self.isValid(s, index, j):
                    currentPart.append(s[index:j+1]) # add + 1 to get rid of the off by 1 error
                    DFS(j + 1)
                    currentPart.pop()

        DFS(0)
        return output

    def isValid(self, s, l, r):
        # takes string, left boundary, right boundary, checks if string is Palindrome
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True
