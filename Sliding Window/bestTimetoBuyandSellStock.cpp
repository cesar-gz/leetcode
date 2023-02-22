/*

121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
*/
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int leftPointer = 0;
        int rightPointer = 1;
        int maxProfit = 0;

        while(rightPointer < prices.size()){
            if(prices[leftPointer] < prices[rightPointer]){
                int profit = prices[rightPointer] - prices[leftPointer];
                maxProfit = max(maxProfit, profit);
            }
            else{
                leftPointer = rightPointer;
            }
            rightPointer += 1;
        }

        cout << "\nIf we buy on day " << leftPointer + 1 << " the price is $" << prices[leftPointer] << "." << endl;
        cout << "Then if we sell on day " << rightPointer - 1 << " the price is $" << prices[rightPointer -2] << "." << endl;
        cout << "Therefore our max profit would be $" << maxProfit << endl;

        return maxProfit;
    }
};

int main(){
    Solution answer;

    vector<int> prices{7,1,5,3,6,4};
    int maxProfit = answer.maxProfit(prices);

    prices = {7,6,4,3,1};
    maxProfit = answer.maxProfit(prices);

}