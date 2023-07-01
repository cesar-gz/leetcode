"""
373. Find K Pairs with Smallest Sums

You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u, v) which consists of one element from the first array and one element from the second array.

Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

"""
from heapq import *

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
      heap = []

      for i in range( min(k, len(nums1) ) ):
         for j in range( min(k, len(nums2) ) ):
            if len(heap) < k:
               heappush(heap, (-(nums1[i]+ nums2[j]), nums1[i] , nums2[j]) )
            else:
               if nums1[i] + nums2[j] > -heap[0][0]:
                  break
               else:
                  heappushpop(heap, (-(nums1[i]+ nums2[j]), nums1[i] , nums2[j]) )

      return [[first, second] for (_, first, second) in heap]
