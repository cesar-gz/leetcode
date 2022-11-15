/*
704. Binary Search

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
*/

#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    int search(vector<int>& nums, int target) {
        int leftPtr = 0;                // going to look at the beginning of the array
        int rightPtr = size(nums) -1;   // going to look at the end of the array
        int midPoint;

        while(leftPtr <= rightPtr){
            midPoint = leftPtr + ((rightPtr-leftPtr)/2);  // mid is defined this way to avoid integer overflow in the case of large ints

            if(nums[midPoint] > target){
                rightPtr = midPoint - 1;     // we are looking at the left side of midpoint in the array
            }
            else if(nums[midPoint] < target){
                leftPtr = midPoint + 1;     // we are looking at the right side of mid point in the array
            }
            else{
                // we found the target
                return midPoint;
            }
        }

        // target was not found after searching the nums array
        return -1;
    }
};

int main(){
    vector<int> nums{-1,0,3,5,9,12};
    int target = 9;

    Solution answer;

    int index = answer.search(nums, target);

    if(nums[index] = target){
        cout << target << " exists in nums and its index is " << index << endl;
    }
    else if(index = -1){
        cout << target << " does not exist in nums so we returned " << index << endl;
    }

    return 0;
}