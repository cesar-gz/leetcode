"""
735. Asteroid Collision

We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size,
and the sign represents its direction (positive meaning right, negative meaning left).
Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions.

If two asteroids meet, the smaller one will explode.
If both are the same size, both will explode.
Two asteroids moving in the same direction will never meet.
"""

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        case 1: keep crushing until no more smaller asteroids
        case 2: push to stack if empty, or meet a negative asteroid
        case 3: destroy both if they're equal mass
        case 4: destroy incoming negative asteroid if it meets a larger positive asteroid

        """
        stack = []

        for asteroid in asteroids:
            # if the stack is not empty, we need to consider if we got case 4
            while stack and stack[-1] > 0 and asteroid < 0:
                # determine which asteroids are exploding
                if abs(stack[-1]) < abs(asteroid):
                    stack.pop()
                    # considered asteroid might still destroy others so keep checking
                    continue
                elif abs(stack[-1]) == abs(asteroid):
                    stack.pop()
                break
            # if stack is empty, or cases 1-3, just append
            else:
                stack.append(asteroid)

        return stack
