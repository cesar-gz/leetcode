/**
104. Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.

* Definition for a binary tree node.
*/

#include<algorithm>
#include<queue>
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
    int maxDepth(TreeNode* root) {
        
        // using Depth First Search and recursion

        // base case
        if(root == nullptr){
            return 0;
        }
        return 1 + max(maxDepth(root->left), maxDepth(root->right));
    }

    int maxDepth2(TreeNode* root) {
        // using Breath First Search and a queue
        
        if(root == nullptr){
            return 0;
        }
        
        queue<TreeNode*> q;
        q.push(root);
        int level = 0;

        while(q.empty() != true){
            int size = q.size();
            for(int i = 0; i<size; i++){
                TreeNode* node = q.front();
                q.pop();
                if(node->left != nullptr){
                    q.push(node->left);
                }
                if(node->right != nullptr){
                    q.push(node->right);
                }
            }
            level += 1;
        }
        return level;
    }
};