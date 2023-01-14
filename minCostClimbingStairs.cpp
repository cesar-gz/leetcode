/*
746. Minimum Cost Climbing Stairs

You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor

*/
#include <vector>
using namespace std;

class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        // add 0 to the end of array to simulate the top floor of stairs
        cost.push_back(0);

        // start from the second to last element in the array,
        // move backwards until we hit the end of array,
        // and decrement by 1 for each loop
        for(int i = size(cost)-3; i > -1; i--){
            cost[i] = min(cost[i]+cost[i+1], cost[i]+cost[i+2]);
        }

        return min(cost[0], cost[1]);
    }
};