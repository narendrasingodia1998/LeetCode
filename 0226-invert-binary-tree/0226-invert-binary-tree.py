# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        temp1=self.invertTree(root.left)
        temp2=self.invertTree(root.right)
        root.left,root.right=temp2,temp1
        return root