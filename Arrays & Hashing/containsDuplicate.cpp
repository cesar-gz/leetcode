/*
problem 217. Contains Duplicate
Given an integer array nums, 
return true if any value appears at least twice in the array, 
and return false if every element is distinct.
*/

#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set <int> hashset;

        for(int j=0; j<size(nums); j++){
            if(hashset.find(nums[j]) == hashset.end()){     // if element is not in hashset, insert it
                hashset.insert(nums[j]);
            }
            else{
                return true;
            }
        }
        return false;                               // went through given list, no duplicates found, return false
    }
};

int main(){

    Solution answer;

    vector<int> testCase1{1,2,3,1};
    bool the = answer.containsDuplicate(testCase1);
    cout << the << endl;

    vector<int> testCase2{1,2,3,4};
    the = answer.containsDuplicate(testCase2);
    cout << the << endl;

    vector<int> testCase3{1,1,1,3,3,4,3,2,4,2};
    the = answer.containsDuplicate(testCase3);
    cout << the << endl;

    return 0;
}