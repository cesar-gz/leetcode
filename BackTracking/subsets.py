"""
78. Subsets

Given an integer array nums of unique elements, return all possible
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.


"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []

        subset = []

        def DFS(index):
            if index >= len(nums): # we are out of bounds
                output.append(subset.copy())
                return

            # decision to include nums[i]
            subset.append(nums[index])
            DFS(index + 1)

            # decision not to include nums[i]
            subset.pop()
            DFS(index + 1)

        DFS(0)
        return output
