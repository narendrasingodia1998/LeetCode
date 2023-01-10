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
    bool iterative(TreeNode* p,TreeNode* q){
        queue<pair<TreeNode*,TreeNode*>> qu;
        qu.push({p,q});
        while(!qu.empty()){
            auto temp=qu.front();
            qu.pop();
            if(temp.first==NULL&&temp.second==NULL){
                continue;
            }
            if(temp.first==NULL||temp.second==NULL){
                return false;
            }
            if(temp.first->val!=temp.second->val){
                return false;
            }
            qu.push({temp.first->left,temp.second->left});
            qu.push({temp.first->right,temp.second->right});
        }
        return true;
    }
    bool isSameTree(TreeNode* p, TreeNode* q) {
        //return recursive(p,q);
        return iterative(p,q);
    }
};