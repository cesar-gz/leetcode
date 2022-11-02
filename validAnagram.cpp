/*
problem 242 Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
*/
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        // first sort both strings
        sort(s.begin(), s.end());               //begin() will take the initial position
        sort(t.begin(), t.end());               //end() takes the final position, sorts in that range order

        // compare strings
        if(s == t){
            return true;
        }
        return false;
    }
};

int main(){
    string test1 = "anagram";
    string test2 = "nagaram";
    string test3 = "rat";
    string test4 = "car";
    string test5 = "clinteastwood";
    string test6 = "oldwestaction";

    Solution answer;

    bool the = answer.isAnagram(test1, test2);
    cout << the << endl;

    the = answer.isAnagram(test3, test4);
    cout << the << endl;

    the = answer.isAnagram(test5, test6);
    cout << the << endl;

    return 0;
}