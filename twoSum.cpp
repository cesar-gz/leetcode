/*
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
*/

#include <vector>
#include <iostream>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // will hold <value, index of nums array>
        unordered_map<int,int> hashMap;
        int difference;

        for(int i=0; i < size(nums); i++){
            difference = target - nums[i];
            if(hashMap.find(difference) != hashMap.end()){      // if you find the difference in the hashMap
                return {hashMap[difference], i};
            }
            hashMap.insert(pair<int,int>{nums[i],i});           // if the value isn't there insert value and index into the hashMap
        }
        return {};
    }
};

int main(){
    Solution answer;

    vector<int> nums{2,15,11,7};
    int target = 9;

    vector<int> indexes{answer.twoSum(nums, target)};

    cout << nums.at(indexes[0]) << " + " << nums.at(indexes[1]) << " = " << target << endl;

    return 0;
}