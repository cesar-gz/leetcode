"""
347. Top K Elements

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

psuedocode: 
    create hashmap that tracks
    create an empty array of arrays, that is the size of the input array
    iterate through input array, adding the each count of a element to the empty array, adding 0 if it does not exist
    iterate through the hash key value pairs, adding the count to the appropriate index
    create empty output array
    iterate through not so empty array, adding the lowest number of counts first in ascending order to output array, and stopping until you reach k
        once k is reached, return output array

"""

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        frequency = [[] for i in range(len(nums) + 1)]

        for number in nums:
            count[number] = 1 + count.get(number, 0)        # if the number doesn't exist, then default value is 0
        
        for number,c in count.items():                      # for every key value pair
            frequency[c].append(number)                          # this value of number exists c amount of times
        
        result = []
        for i in range(len(frequency)-1, 0, -1):            # iterate through array, start in reverse order, end at 0
            for number in frequency[i]:
                result.append(number)
                if len(result) == k:
                    return result
                
"""
Test Cases:
"""
# Input
nums = [1,1,1,2,2,3]
k = 2
# Output: [1,2]
testCase = Solution()
print(testCase.topKFrequent(nums, k))

# Input
nums = [1]
k = 1
# Output: [1]
print(testCase.topKFrequent(nums, k))
