/*
1046.

You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.
*/

#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int> minHeap(stones.begin(), stones.end());
        while(minHeap.size()>1){

            int firstStone = minHeap.top();
            minHeap.pop();
            int secondStone = minHeap.top();
            minHeap.pop();

            if(secondStone != firstStone){
                minHeap.push(firstStone-secondStone);
            }
        }

        minHeap.push(0);
        return minHeap.top();
        //return minHeap.empty()? 0: minHeap.top();
    }
};