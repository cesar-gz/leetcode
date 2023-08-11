"""
51. N-Queens

The n-queens puzzle is the problem of placing n queens on an n x n chessboard
such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.
You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement,
where 'Q' and '.' both indicate a queen and an empty space, respectively.
"""


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # 3 sets to keep track where we can place queens
        col = set()           # will track which qs are in which cols
        positiveDiag = set()  # will track which qs are in the ascending diagonals  (r+c)
        negativeDiag = set()  # will track which qs are in the descending diagonals (r-c)
        output = []
        board = [["."] * n for i in range(n)]

        def backtrack(row):
            if row == n:
                copy = [ "".join(r) for r in board]
                output.append(copy)
                return

            for c in range(n):
                if c in col or (row+c) in positiveDiag or (row-c) in negativeDiag:
                    continue # there is a queen stopping us from place another queen

                col.add(c)
                positiveDiag.add(row + c)
                negativeDiag.add(row - c)
                board[row][c] = "Q"

                backtrack(row + 1)

                col.remove(c)
                positiveDiag.remove(row + c)
                negativeDiag.remove(row - c)
                board[row][c] = "."

        backtrack(0)
        return output
