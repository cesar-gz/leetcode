/*
136. Single Number
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
*/

#include <vector>
using namespace std;

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int result = 0; // n ^(exclusive or) 0 = n
        for(int i = 0; i < size(nums); i++){
            result = nums[i] ^ result;
        }
        return result;
    }
};