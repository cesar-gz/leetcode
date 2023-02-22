/**
 * 110. Balanced Binary Tree
 * 
 * Given a binary tree, determine if it is height-balanced.
 * 
 * Definition for a binary tree node.
 */
#include <utility>
#include <cstdlib>
#include <algorithm>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    bool isBalanced(TreeNode* root) {
        pair<bool, int> answer;
        answer = depthFirstSearch(root);
        return answer.first;
    }

    pair<bool, int>depthFirstSearch(TreeNode* root){
        
        if(root == nullptr){
            pair<bool, int> values;
            values = make_pair(true, 0);
            return values;
        }
        
        pair<bool, int> left;
        pair<bool, int> right;
        left = depthFirstSearch(root->left);
        right = depthFirstSearch(root->right);

        int balance = abs(left.second - right.second);
        if(left.first == true && right.first == true && balance <= 1){
            pair<bool, int> balanced;
            balanced = make_pair(true, 1 + max(left.second, right.second));
            return balanced;
        }
        pair<bool, int> notBalanced;
        notBalanced = make_pair(false, 2);
        return notBalanced;
    }
};