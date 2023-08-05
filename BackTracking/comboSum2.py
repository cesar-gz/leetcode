"""
40. Combination Sum II

Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.
Note: The solution set must not contain duplicate combinations.
"""


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort() # to help remove duplicates later
        output = []

        def backtrack(currentCombo, startPosition, target):
            if target == 0:
                output.append(currentCombo[::]) # append a copy
            if target <= 0:
                return

            prev = -1

            for index in range(startPosition, len(candidates)):
                if candidates[index] == prev:
                    continue
                currentCombo.append(candidates[index])
                backtrack(currentCombo, index + 1, target - candidates[index])
                currentCombo.pop()

                prev = candidates[index]

        backtrack([], 0, target)
        return output
