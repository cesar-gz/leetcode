/**
 * 100. Same Tree
 * 
 * Given the roots of two binary trees root and subRoot, return true if there is a root of root 
 * with the same structure and node values of subRoot and false otherwise.
 *
 * A root of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. 
 * The tree tree could also be considered as a root of itself.
 * 
 * Definition for a binary tree node.
 */
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
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        if(subRoot == nullptr){
            return true;
        }
        if(root == nullptr){
            return false;
        }
        if(isSameTree(root, subRoot) == true){
            return true;
        }

        bool checkLeftSide = isSubtree(root->left, subRoot);
        bool checkRightSide = isSubtree(root->right, subRoot);

        if(checkLeftSide || checkRightSide == true){
            return true;
        }
        else{
            return false;
        }
    }

    bool isSameTree(TreeNode* subTree, TreeNode* tree){
        if(subTree == nullptr && tree == nullptr){
            return true;
        }
        if(subTree != nullptr && tree != nullptr && subTree->val == tree->val){
            bool leftChild = isSameTree(subTree->left, tree->left);
            bool rightChild = isSameTree(subTree->right, tree->right);
            if(leftChild == true && rightChild == true){
                return true;
            }
            else{
                return false;
            }
        }
        else{
            return false;
        }
    }
};

