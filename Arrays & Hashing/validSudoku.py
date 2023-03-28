"""
36. Valid Sudoku
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
Each row must contain the digits 1-9 w/out repetition
Each column must contain the digits 1-9 w/out repetition
Each of the 3x3 sub-boxes of the grid must contain the digits 1-9 w/out repetition
"""

import collections

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        columns = collections.defaultdict(set)                  # create hash map, the set is the values
        rows = collections.defaultdict(set)                     # another hashmap for rows
        squares = collections.defaultdict(set)                  # to help solve the 3rd precondition in the constraints, key = (row/3, cow/3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":                          # if this is an empty space, we can skip it
                    continue
                if (board[r][c] in rows[r]                      # if the current number is already in the same row or column, this is a duplicate
                    or
                    board[r][c] in columns[c]
                    or
                    board[r][c] in squares[(r // 3, c // 3)]):  # or if the current number is already in the 3x3 sub square, return false
                    return False
                columns[c].add(board[r][c])                     # we did not find duplicates, we will update our positions
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])      # we divide by 3 to verify we are in the correct sub square

        return True
