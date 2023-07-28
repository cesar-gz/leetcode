"""
130. Surrounded Regions

Given an m x n matrix board containing 'X' and 'O',
capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.
"""

class Solution:
    def solve(self, board: List[List[str]]) -> None:
      rows, cols = len(board), len(board[0])

      def DFS(r, c):
         if r < 0 or c < 0 or r == rows or c == cols or board[r][c] != "O":
            return
         board[r][c] = "T"
         DFS(r + 1, c)
         DFS(r - 1, c)
         DFS(r, c + 1)
         DFS(r, c - 1)

      #phase 1: capture unsurrounded regions (Os to Ts)
      for r in range(rows):
         for c in range(cols):
            if ( board[r][c] == "O" and ( r in [0, rows-1] or c in [0, cols-1] ) ):
               # if board cell has a O, and is in the one of the borders of the board
               DFS(r,c)

      #phase 2: capture surrounded regions (Os to Xs)
      for r in range(rows):
         for c in range(cols):
            if board[r][c] == "O":
               board[r][c] = "X"

      #phase 3: uncapture unsurrounded regions (Ts back to Os)
      for r in range(rows):
         for c in range(cols):
            if board[r][c] == "T":
               board[r][c] = "O"
