"""
46. Permutations
Given an array nums of distinct integers, return all the possible permutations.
You can return the answer in any order.
"""


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []

        # base case
        if len(nums) == 1:
            return [nums.copy()]

        for i in range(len(nums)):
            n = nums.pop(0) # pop the first value of array

            permutations = self.permute(nums)

            for perm in permutations:
                perm.append(n)

            output.extend(permutations)
            nums.append(n)
        return output
