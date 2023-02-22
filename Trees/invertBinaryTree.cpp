/**
 * 
 * 226. Invert Binary Tree
 * 
 * Given the root of a binary tree, invert the tree, and return its root
 * 
 * Definition for a binary tree node.
 */
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
    TreeNode* invertTree(TreeNode* root) {
        
        // base case
        if(root == nullptr){
            return nullptr;
        }

        // swap children
        TreeNode* tempVar = root->left;
        root->left = root->right;
        root->right = tempVar;

        // recursive calls
        invertTree(root->left);
        invertTree(root->right);
        return root;
    }
};