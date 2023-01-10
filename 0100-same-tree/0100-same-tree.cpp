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
    bool isSameTree(TreeNode* p, TreeNode* q) {
        //Base Condition
        if(p==NULL&&q==NULL){
            return true;
        }
        if(p==NULL){
            return false;
        }
        if(q==NULL){
            return false;
        }
        //General Condition
        if(p->val!=q->val){
            return false;
        }
        if(!isSameTree(p->left,q->left)){
            return false;
        }
        return isSameTree(p->right,q->right);
    }
};