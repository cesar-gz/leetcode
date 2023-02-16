/*268. Missing Number

Given an array nums containing n distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array.

Constraints:

n == nums.length
1 <= n <= 104
0 <= nums[i] <= n
All the numbers of nums are unique.

*/

#include <vector>
using namespace std;

class Solution {
public:

    // basically going to be: sum(0,1,2, ... n) - sum(input)
    int missingNumber(vector<int>& nums) {
        // grab the nth value
        int result = size(nums);

        // loop through the vector
        for(int i = 0; i < size(nums); i++){
            // the result will end up being equal to the number in the vector that is missing
            result += (i - nums[i]);
        }

        return result;
    }
};