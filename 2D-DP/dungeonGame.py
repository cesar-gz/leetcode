"""
174. Dungeon Game

The demons had captured the princess and imprisoned her in the bottom-right corner of a dungeon.
The dungeon consists of m x n rooms laid out in a 2D grid.
Our valiant knight was initially positioned in the top-left room and must fight his way through dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer.
If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons (represented by negative integers),
so the knight loses health upon entering these rooms; other rooms are either empty (represented as 0) or
contain magic orbs that increase the knight's health (represented by positive integers).

To reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

Return the knight's minimum initial health so that he can rescue the princess.

Note that any room can contain threats or power-ups,
even the first room the knight enters and the bottom-right room where the princess is imprisoned.

"""

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        height, width = len(dungeon), len(dungeon[0])
        m, n = height - 1, width - 1

        dp = dungeon  # dynamic programming array

        # princesses spot
        dp[m][n] = max(1, 1 - dp[m][n])

        # fill out dp array, setting 1s where the knight would not receive damage
        for r in range(m-1, -1, -1):
            dp[r][n] = max(1, dp[r+1][n] - dp[r][n])

        for c in range(n-1, -1, -1):
            dp[m][c] = max(1, dp[m][c+1] - dp[m][c])

        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                dp[r][c] = max( 1, min(dp[r+1][c], dp[r][c+1]) - dp[r][c] )

        return dp[0][0]
