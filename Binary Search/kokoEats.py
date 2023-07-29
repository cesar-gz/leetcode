"""
875. Koko Eating Bananas

Koko loves to eat bananas. There are n piles of bananas,
the ith pile has piles[i] bananas. The guards have gone and will
come back in h hours.

Koko can decide her bananas-per-hour eating speed of k.
Each hour, she chooses some pile of bananas and eats k bananas
from that pile. If the pile has less than k bananas,
she eats all of them instead and will not eat any more bananas
during this hour.

Koko likes to eat slowly but still wants to finish
eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

"""

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        leftPtr, rightPtr = 1, max(piles)
        result = rightPtr

        # start binary search
        while leftPtr <= rightPtr:
            k = (leftPtr + rightPtr) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)

            if hours <= h:
                # eating rate was too big
                result = min(result, k)
                rightPtr = k - 1
            else:
                # eating rate was too small
                leftPtr = k + 1
        return result
