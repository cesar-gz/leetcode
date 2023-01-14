/*
202. Happy Number

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.

Repeat the process until the number equals 1 (where it will stay), 
or it loops endlessly in a cycle which does not include 1.

Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not
*/

#include <unordered_set>
using namespace std;

class Solution {
public:
    bool isHappy(int n) {
        // create a hashSet which will track distinct values we have used
        unordered_set<int> numbersVisited;

        // if n is not in the hashSet
        while(numbersVisited.find(n) == numbersVisited.end()){
            numbersVisited.insert(n);
            n = sumOfSquares(n);
            if(n == 1){
                return true;
            }
        }
        // we didn't reach 1, and hit a cycle of numbers with no 1 in it
        return false;
    }

    int sumOfSquares(int n){
        int output = 0;

        // 1 % 10 = 0, 1 / 0 = 0
        // we use to modulus to get the ten's place digit
        // we use int division to get the one's place digit
        while(n != 0){
            int digit = n % 10;
            digit = digit*digit;
            output += digit;
            n = n / 10;
        }

        return output;
    }
};