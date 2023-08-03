"""
39. Combination Sum

Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times.
Two combinations are unique if the frequency of at least one of the chosen numbers is different.

"""


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []

        def DFS(index, currentCombo, total):
            # base cases
            if total == target:
                output.append(currentCombo.copy()) # add a copy because we still using it
                return
            if index >= len(candidates) or total > target:
                return # if index > len of array then out of bounds error

            # decision where we can include the candidate
            currentCombo.append(candidates[index])
            DFS(index, currentCombo, total + candidates[index])

            # decision where we cant include the candidate
            currentCombo.pop()
            DFS(index + 1, currentCombo, total)

        DFS(0, [], 0)
        return output
