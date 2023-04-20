"""
Submission for Cesar Gutierrez
"""

def soccer_exhaustive(matrixG):
    """
    Solve a soccer game where one team starts in position [0,0] of a matrix, and wins when it reaches the
    bottom right corner end of the matrix. The field is by rows x column, the player can only move down
    a row or right a column. The player can not pass through enemy players. Solve using a exhaustive
    approach.
    """
    r, c = 0, 0             # row, column
    for row in matrixG:
        r += 1
    for col in matrixG:
        c += 1

    print(r)
    print("")
    print(c)

def soccer_dyn_prog(matrixF):
    """
    Same as both except solve using a dynamic programming approach.
    """
    pass



""" Test Cases """

# "X"s are un passable enemy players, "." are free spaces
grid = [[".",".",".",".",".",".","X",".","X"],
        ["X",".",".",".",".",".",".",".","."],
        [".",".",".","X",".",".",".","X","."],
        [".",".","X",".",".",".",".","X","."],
        [".","X",".",".",".",".","X",".","."],
        [".",".",".",".","X",".",".",".","."],
        [".",".","X",".",".",".",".",".","X"],
        [".",".",".",".",".",".",".",".","."]]

# optimal solution is supposed to be 102
print(soccer_exhaustive(grid))
print(soccer_dyn_prog(grid))
