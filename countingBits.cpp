/*
338. Counting Bits

Given an integer n, return an array ans of length n + 1
such that for each i (0 <= i <= n), ans[i] is the number of 1's
in the binary representation of i.

*/
#include <vector>
using namespace std;

class Solution
{
public:
  vector<int> countBits(int n)
  {
    // create an array thats sized n+1 and is initialized to all 0s
    vector<int> answer(n + 1, 0);
    int offset = 1;                   // will change based off the current power of 2
    for (int x = 1; x < n + 1; x++){
      if(offset*2 == x){
        offset = x;
      }
      answer[x] = answer[x - offset] + 1;
    }
    return answer;
  }
};
