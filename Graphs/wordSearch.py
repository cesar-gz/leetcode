"""
79. Word Search
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring.
The same letter cell may not be used more than once.
"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        # if the word has more characters than the board
        if rows*cols < len(word):
            return False

        # used to see if the word is at the starting position
        def check(i, j, k):
            # check if the character is out of bounds or the character does not match
            if i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] != word[k]:
                return False

            # if we reached the end of the word
            if k == len(word) - 1:
                return True

            # mark the character as visited by replacing it with a space character
            temp = board[i][j]
            board[i][j] = ' '

            # check if the rest of the word exists in any of the adjacent positions
            found = check(i - 1, j, k + 1) or check(i + 1, j, k + 1) or check(i, j - 1, k + 1) or check(i, j + 1, k + 1)

            board[i][j] = temp

            return found

        # check each starting point for the full string using DFS, return True if found
        for i in range(len(board)):
            for j in range(len(board[0])):
                if check(i, j, 0):
                    return True
        return False
    # O(N * M * 3^L) Time we need to start at each character in the board, then performing a DFS on 3 possible paths from each char
    # O(L) Space where we need to store the length of our word as depth in our recursion stack
