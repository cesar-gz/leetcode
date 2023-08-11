"""
322. Coin Change

You are given an integer array coins representing coins of different denominations and
an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1) # initialize length of amount + 1, the default val for ea elem is amount + 1
        dp[0] = 0 # base case -> it takes 0 coins to get the amount of 0

        for a in range(1, amount + 1): # bottom up approach
            for c in coins:
                if a - c >= 0:
                    # we can continue searching, possible solution
                    dp[a] = min(dp[a], 1 + dp[a-c])

        return dp[amount] if dp[amount] != amount + 1 else -1 # return the amount if it is not the preset default value we gave it
    # O(amount * len(coins)) Time
    # O(amount) Space for the dp Array
