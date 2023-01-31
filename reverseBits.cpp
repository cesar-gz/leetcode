/*

190. Reverse Bits

Reverse bits of a given 32 bits unsigned integer.

*/


#include <stdint.h> //for uint32_t
#include <stdio.h>  // for bit shifting
using namespace std;

class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t answer = 0;
        for(int x = 0; x < 32; x++){
            int bit = (n >> x) & 1;             // (bit shift n to the right) then logical "and" it by 1 to get either a 0 or 1 bit
            answer = answer | (bit << (31-x));  // bit shift to the left to the correct index location, then logical "or" it to get the 1 if it exists
        }
        return answer;
    }
};