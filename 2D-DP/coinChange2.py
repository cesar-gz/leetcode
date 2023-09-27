"""
518. Coin Change 2

You are given an integer array coins representing coins
of different denominations and an integer amount representing
a total amount of money.

Return the number of combinations that make up that amount.
If that amount of money cannot be made up by any combination of the coins,
return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.
"""

class Solution:
    # dynamic programming solution using a cache
    def change(self, amount: int, coins: list[int]) -> int:
        dp = {}

        def DFS(index, a):
            if a == amount:
                # we found our target amount
                return 1
            if a > amount:
                # we cannot possible sum up to the amount
                return 0
            if index == len(coins):
                # we are out of bounds, no coins available
                return 0
            if (index, a) in dp:
                # already computed, return it
                return dp[(index,a)]

            # two decisions: use the coin at index i, and skip the current coin
            dp[(index, a)] = DFS(index, a + coins[index]) + DFS(index + 1, a)
            return dp[(index,a)]

        return DFS(0,0)
    # O(m*n) Time and Space, where m is the amount of coins, and n is the amount
