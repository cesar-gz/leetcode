/**
 * 703. Kth Largest Element in a stream
 * 
 * a stream means we can continue to add numbers to the list
 * 
 * Design a class to find the kth largest element in a stream
 * 
 * not the kth distinct element
 * 
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */

// I needed help and dove into the solutions section for help

#include <vector>
#include <queue>
using namespace std;

class KthLargest {
public:
    priority_queue<int,vector<int>,greater<int>> minHeap;
    int kth;

    KthLargest(int k, vector<int>& nums) {
        kth = k;
        int x = min(k, (int)nums.size());
        for(int i=0; i<x; i++){
            minHeap.push(nums[i]);
        }
        for(int i=k; i<nums.size(); i++){
            if(nums[i] > minHeap.top()){
                minHeap.pop();
                minHeap.push(nums[i]);
            }
        }
    }
    
    int add(int val) {
        if(minHeap.size() < kth){
            minHeap.push(val);
            return minHeap.top();
        }
        if(val > minHeap.top()){
            minHeap.pop();
            minHeap.push(val);
        }
        return minHeap.top();
    }
};
