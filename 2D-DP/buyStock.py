"""
309. Best Time to Buy Stock with Cooldown

You are given an array prices where prices[i]
is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many
transactions as you like (i.e., buy one and sell one share of the stock multiple times)
with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously
(i.e., you must sell the stock before you buy again).
"""

class Solution:
    # Dynamic Programming solution with cache
    def maxProfit(self, prices: list[int]) -> int:
        # if buy then the key is index i + 1
        # if sell then the key is index i + 2, 2 because we have to cooldown next day
        dp = {} # key = (i, buying/selling boolean), value = max profit

        def DFS(i, buying):
            if i >= len(prices):
                # out of bounds, empty array of prices
                return 0

            if (i, buying) in dp:
                return dp[(i, buying)]

            if buying:
                # first decision is to sell as next move, subtract price of stock
                buy = DFS(i + 1, not buying) - prices[i]
                # other decision is to cooldown
                cooldown = DFS(i + 1, buying)
                dp[(i,buying)]= max(buy, cooldown)
            else:
                sell = DFS(i + 2, not buying) + prices[i]
                cooldown = DFS(i + 1, buying)
                dp[(i, buying)] = max(sell, cooldown)
            return dp[(i, buying)]

        return DFS(0, True)
