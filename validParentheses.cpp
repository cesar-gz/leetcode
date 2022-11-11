/*
20. Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
*/
#include <string>
#include <iostream>
#include <unordered_map>
#include <stack>
using namespace std;

class Solution {
public:
    bool isValid(string s) {
        stack<char> stack;
        unordered_map<char,char> hashMap = {
            {')', '('},
            {']', '['},
            {'}', '{'}
        };

        for(int i = 0; i < s.length(); i++){    // iterate through given string
            char temp = s.at(i);
            if(hashMap.count(temp)){
                // if the char from the string is in the hashmap
                if(stack.empty() == false && (stack.top() == hashMap.find(temp)->second) ){
                    // if the stack is not empty, and the top of the stack is = the value of the key
                    stack.pop();
                }
                else{
                    return false;   // no match
                }
            }
            else{
                stack.push(temp);
            }
        }
        
        if(stack.empty()){
            return true;
        }
        else{
            return false;
        }
    }
};

int main(){
    string s = "()";
    Solution answer;
    bool the;

    the = answer.isValid(s);
    cout << the << endl;

    s = "()[]{}";
    the = answer.isValid(s);
    cout << the << endl;

    s = "(]";
    the = answer.isValid(s);
    cout << the << endl;

    return 0;
}