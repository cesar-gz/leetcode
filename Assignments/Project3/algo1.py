"""
Submission for Cesar Gutierrez
"""
import time

def soccer_exhaustive(matrixG):
    """
    Solve a soccer game where one team starts in position [0,0] of a matrix, and wins when it reaches the
    bottom right corner end of the matrix. The field is by rows x column, the player can only move down
    a row or right a column. The player can not pass through enemy players. Solve using a exhaustive
    approach.
    """
    start_time = time.time()

    r = len(matrixG)        # number of rows in matrix
    c = len(matrixG[0])     # number of cols in matrix

    length = r + c - 2
    counter = 0
    i, j = 0, 0

    for bits in range(0, pow(2, length) ):
      candidate = []
      for k in range(0, length):
         bit = (bits >> k) & 1
         if bit == 1:
            candidate.append( (i,j+1) )
         else:
            candidate.append( (i+1, j) )
      if isValid(candidate, matrixG, r, c):
        counter += 1

    # to get a measure of time
    print("--- %s seconds ---" % (time.time() - start_time))

    return counter

def isValid(path, grid, row, col):
   """ helper function for soccer_exhaustive()"""
   x, y = 0, 0
   for move in path:
      # counting if we are within the grid still
      if move[0] < move[1]:         # if the move is "right"
         y += 1
      else:                         # the move is "down"
         x += 1
      # if the candidate stays inside the grid, never crosses an X cell, and
      # ends at the bottom right corner of the matrix
      if x >= row or y >= col or grid[x][y] == "X":
         return False
   return True


def soccer_dyn_prog(matrixF):
  """ same as the problem above, but solve using a dynamic programming approach"""

  start_time = time.time()

  if matrixF[0][0] == "X":
     # corner case where the first starting cell is un passable
     return 0

  r = len(matrixF)        # number of rows in matrix
  c = len(matrixF[0])     # number of cols in matrix

  newMatrix = [[0 for j in range(c)] for i in range(r)] # initialized to zeroes

  # base case
  newMatrix[0][0] = 1

  # general case
  for i in range(r):
     for j in range(c):
        if matrixF[i][j] == "X":
           newMatrix[i][j] = 0
           continue
        above, left, = 0 , 0
        if i > 0 and matrixF[i-1][j] == "." :
           above = newMatrix[i-1][j]
        if j > 0 and matrixF[i][j-1] == "." :
           left = newMatrix[i][j-1]
        newMatrix[i][j] += above + left

  # to get a measure of time
  print("--- %s seconds ---" % (time.time() - start_time))

  return newMatrix[r-1][c-1]


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
