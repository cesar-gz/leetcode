/*
58. Maximum Subarray
Given an integer array nums, find the subarray
 with the largest sum, and return its sum.
*/
#include <algorithm>
using namespace std;

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int maxSubArr = nums[0];

        int currentSum = 0;

        // starting going through nums
        for(int i = 0; i < size(nums); i++){
            // if we start getting a negative subarray, reset-forget and move on to a new subarray
            if(currentSum < 0){
                currentSum = 0;
            }
            // start adding the subArray
            currentSum += nums[i];

            maxSubArr = max(maxSubArr, currentSum);
        }
        return maxSubArr;
    }
};