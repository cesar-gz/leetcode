"""
638. Shopping Offers

In LeetCode Store, there are n items to sell. Each item has a price.
However, there are some special offers, and a special offer consists of one or more different kinds of items with a sale price.

You are given an integer array price where price[i] is the price of the ith item,
and an integer array needs where needs[i] is the number of pieces of the ith item you want to buy.

You are also given an array special where special[i] is of size n + 1 where special[i][j]
is the number of pieces of the jth item in the ith offer and special[i][n]
(i.e., the last integer in the array) is the price of the ith offer.

Return the lowest price you have to pay for exactly certain items as given,
where you could make optimal use of the special offers.
You are not allowed to buy more items than you want, even if that would lower the overall price.
You could use any of the special offers as many times as you want.

"""

class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        dp = {}

        def DFS(needs):
            if sum(needs) == 0:
                return 0

            key = tuple(needs)
            if key in dp:
                return dp[key]

            best = self.buyOut(needs, price)

            for offer in special:
                newNeeds = self.canTake(offer, needs[:])
                if newNeeds:
                    best = min(best, offer[-1] + DFS(newNeeds))

            dp[key] = best
            return best

        return DFS(needs)

    def buyOut(self, needs, prices):
        return sum([n*p for n, p in zip(needs, prices)])

    def canTake(self, offer, needs):
        for i in range(len(needs)):
            needs[i] -= offer[i]
            if needs[i] < 0:
                return []
        return needs
