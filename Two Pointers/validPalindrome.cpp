// question 125 [easy]

/*
Given a string s, return true if it is a palindrome, or false otherwise.
*/

#include <string>
#include <iostream>
using namespace std;

class Solution {
public:
    bool isPalindrome(string s) {
        int leftPointer = 0;                // start left pointer at the beginning of the string
        int rightPointer = s.length()-1;      // start right pointer at the end of the string

        while(leftPointer < rightPointer){
            while( (leftPointer < rightPointer) && ( isalnum(s.at(leftPointer)) == false ) ){
                leftPointer += 1;   // traverse pass the non alpha numerical characters on the left side of string
            }
            while( (rightPointer > leftPointer) && ( isalnum(s.at(rightPointer)) == false) ){
                rightPointer -= 1;  // traverse pass the non alpha numerical characters on the right side of string
            }
            if( tolower(s.at(leftPointer)) != tolower(s.at(rightPointer)) ){
                return false;       // left character that is pointed != right character that is pointed, then this is not a palindrome
            }
            leftPointer += 1;       // move left pointer forwards
            rightPointer -= 1;      // move right pointer backwrds
        }
        return true;
    }
};

int main(){
    string palin1 = "A man, a plan, a canal: Panama";
    string palin2 = "race a red car";

    Solution answer;

    bool the = answer.isPalindrome(palin1);
    if(the == true){
        cout << palin1 << " is a palindrome.\n";
    }

    the = answer.isPalindrome(palin2);
    if(the == false){
        cout << palin2 << " is not a palindrome.";
    }
}