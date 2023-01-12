/*
70. Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
*/

// the number of disinct ways of climbing stairs, with 1 or 2 steps, ends up becoming the reverse
// of the fibonacci sequence. Reverse in the way we start the last two values as 1 and 1, and
// begin the sequence going to the first index, or the first starting point

class Solution {
public:
    int climbStairs(int n) {
        int stepOne = 1;
        int stepTwo = 1;

        for(int i=0; i < n-1; i++){
            int temp = stepOne;
            stepOne = stepOne + stepTwo;
            stepTwo = temp;
        }

        return stepOne;
    }
};