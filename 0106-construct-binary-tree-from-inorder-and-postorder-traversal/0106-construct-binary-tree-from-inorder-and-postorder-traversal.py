# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """
        #Time Complexity is O(n*n)
        #Base Condition
        if not inorder:
            return None
        val=postorder[-1]
        index=0
        while index<len(inorder) and inorder[index]!=val:
            index+=1
        root=TreeNode(postorder[-1])
        root.left=self.buildTree(inorder[0:index],postorder[0:index])
        root.right=self.buildTree(inorder[index+1:],postorder[index:-1])
        return root
        """
        
        def solve(in_start,in_end,post_start,post_end):
            #Base Condition
            if in_start>in_end:
                return None
            val=postorder[post_end]
            index=in_start
            while inorder[index]!=val:
                index+=1
            root=TreeNode(val)
            length=(index-1)-in_start+1
            root.left=solve(in_start,index-1,post_start,post_start+length-1)
            root.right=solve(index+1,in_end,post_start+length,post_end-1)
            return root
        
        n=len(inorder)
        return solve(0,n-1,0,n-1)