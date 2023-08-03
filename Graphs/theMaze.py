"""
490. The Maze

There is a ball in a maze with empty spaces (represented as 0) and walls (represented as 1).
The ball can go through the empty spaces by rolling up, down, left or right, but it won't stop rolling
until hitting a wall. When the ball stops, it could choose the next direction.
Given the m x n maze, the ball's start position and the destination, where start = [startrow, startcol]
and destination = [destinationrow, destinationcol],
return true if the ball can stop at the destination, otherwise return false.

"""

from collections import deque

class Solution:
    def hasPath(self, maze, start, destination):
        rows, cols = len(maze), len(maze[0])
        directions = [ (0,1), (0,-1), (1,0), (-1, 0) ] # up down right left

        def isValid(x, y):
            # return True if the ball is still within the grid and able to roll
            return 0 <= x < rows and 0 <= y < cols and maze[x][y] == 0

        q = deque()
        q.append(start)

        visited = set()
        visited.add(tuple(start))

        while q:
            x, y = q.popleft()
            if [x,y] == destination:
                return True

            for dx, dy in directions:
                nx, ny = x, y

                while isValid(nx + dx, ny+ dy):
                    nx += dx
                    ny += dy

                if (nx, ny) not in visited:
                    q.append( [nx, ny] )
                    visited.add( (nx, ny) )

        return False
