"""
554. Brick Wall
There is a rectangular brick wall in front of you with n rows of bricks.
The ith row has some number of bricks each of the same height (i.e., one unit) but they can be of different widths.
The total width of each row is the same.

Draw a vertical line from the top to the bottom and cross the least bricks.
If your line goes through the edge of a brick, then the brick is not considered as crossed.
You cannot draw a line just along one of the two vertical edges of the wall,
in which case the line will obviously cross no bricks.

Given the 2D array wall that contains the information about the wall,
return the minimum number of crossed bricks after drawing such a vertical line.
"""

class Solution:
    def leastBricks(self, wall: list[list[int]]) -> int:
        #  create a hash map that will map column positions to the count of the gaps between bricks in each row,
        #  set position 0 to have 0 gaps
        countGap = {0:0}

        for row in wall:
            # our current position will be total
            total = 0
            # start iterating through the gaps, except for the last column since that is our restriction
            for brick in row[:-1]:
                total += brick
                # increment the count by if 1 if the position already exists, if it DNE then create it with total as the key, 0 as the default value
                countGap[total] = 1 + countGap.get(total, 0)
        # return the total number of rows, minus the highest count of gaps
        return len(wall) - max( countGap.values() )

# time complexity is linear O(N), where N is the amount of bricks in the wall
# space is linear too, as we create a hash map for each one
