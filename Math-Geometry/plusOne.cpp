/*
66. Plus One

You are given a large integer represented as an integer array digits, 
where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order.
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
*/

#include <vector>
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        reverse(digits.begin(), digits.end());
        int carry = 1;  // the carry the one digit we will use
        int i = 0;      // index of the position of the digit we are examining

        while(carry == 1){
            if(i < size(digits)){
                //while in bounds of the number
                if(digits[i] == 9){
                    //edge case where 999 + 1 should = 1000 and not 99910
                    digits[i] = 0;
                }
                else{
                    digits[i] += 1;
                    carry = 0;
                }
            }
            else{
                //out of bounds
                digits.push_back(1);
                carry = 0;
            }
            i += 1;
        }
        reverse(digits.begin(), digits.end());
        return digits;
    }
};