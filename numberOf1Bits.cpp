/*
191. Number of 1 Bits

Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

*/

#include <stdint.h>
using namespace std;

class Solution {
public:
    int hammingWeight(uint32_t n) {
        int totalCount = 0;         // track the total amount of 1s
        while(n!=0){
            totalCount += n%2;      // if the result is a 1, then increment total count. if the result is 0, don't increment result
            n = n >> 1;             // bit shift to the right by 1
        }
        return totalCount;
    }
};

/*
Another possible solution

    int hammingWeight(uint32_t n) {
        int totalCount = 0;         
        while(n!=0){
            n = n & (n-1);
            totalCount += 1; 
        }
        return totalCount;
    }

*/