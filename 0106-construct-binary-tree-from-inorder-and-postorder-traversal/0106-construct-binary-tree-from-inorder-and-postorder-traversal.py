# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self,inorder,postorder):
        #Base Condition
        if not inorder:
            return
        val=postorder[-1]
        index=0
        while index<len(inorder) and inorder[index]!=val:
            index+=1
        root=TreeNode(postorder[-1])
        root.left=self.solve(inorder[0:index],postorder[0:index])
        root.right=self.solve(inorder[index+1:],postorder[index:-1])
        return root
    
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        #Base Condition
        if not inorder:
            return
        val=postorder[-1]
        index=0
        while index<len(inorder) and inorder[index]!=val:
            index+=1
        root=TreeNode(postorder[-1])
        root.left=self.solve(inorder[0:index],postorder[0:index])
        root.right=self.solve(inorder[index+1:],postorder[index:-1])
        return root