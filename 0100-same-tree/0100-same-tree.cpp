/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool recursive(TreeNode* p,TreeNode* q){
        //Base Condition
        if(p==NULL&&q==NULL){
            return true;
        }
        if(p==NULL||q==NULL){
            return false;
        }
        //General Condition
        return p->val==q->val && isSameTree(p->left,q->left) && isSameTree(p->right,q->right);
    }
    bool isSameTree(TreeNode* p, TreeNode* q) {
        return recursive(p,q);
    }
};