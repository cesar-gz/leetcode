class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        # from math import *
        # create an array which has all the integers from 1 to maxChoosableInteger.
        usable = [x for x in range(1, maxChoosableInteger + 1)]
        if (1 + maxChoosableInteger) * maxChoosableInteger <= desiredTotal:
            return False
        else:
            return self.hint(maxChoosableInteger, desiredTotal, usable, {}, 0)

    def hint(self, maxChoosableInteger, desiredTotal, usable, cache, already):
        if len(usable) == 0:
            return False
        else:
            state = tuple(usable)
            if state in cache:
                return cache[state]   # if we already have it saved, retrieve and return it
            else:
                # otherwise
                cache[state] = False
                if max(usable) + already >= desiredTotal:
                    cache[state] = True
                elif len(usable) > 1 and max(usable) + already >= desiredTotal:
                    cache[state] = False
                else:
                    for x in usable:
                        newState = [y for y in usable if y != x]
                        if not self.hint(maxChoosableInteger, desiredTotal, newState, cache, already + x):
                            cache[state] = True
                            break
                return cache[state]
