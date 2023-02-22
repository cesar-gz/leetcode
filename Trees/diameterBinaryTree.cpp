/**
 * 543. Diameter of Binary Tree
 * 
 * Given the root of a binary tree, return the length of the diameter of the tree.

   The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

   The length of a path between two nodes is represented by the number of edges between them.

 * Definition for a binary tree node.
*/

#include<algorithm>
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
    int result = 0;

    int diameterOfBinaryTree(TreeNode* root) {
        depthFirstSearch(root);
        return result;
    }

    int depthFirstSearch(TreeNode* root){
        if(root == nullptr){
            return -1;
        }
        
        int left = depthFirstSearch(root->left);
        int right = depthFirstSearch(root->right);

        result = max(result, 2 + left + right);
        return 1 + max(left,right);
    }
};