# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bfs(self,root):
        if not root:
            return True
        nullNodeFound=False
        q=deque()
        q.append(root)
        while q:
            node=q.popleft()
            if not node:
                nullNodeFound=True
            else:
                if nullNodeFound:
                    return False
                q.append(node.left)
                q.append(node.right)
        return True
    
    def count(self,root):
        if not root:
            return 0
        return 1+self.count(root.left)+self.count(root.right)
    
    
    def dfs(self,root,i,n):
        if not root:
            return True
        if i>=n:
            return False
        return self.dfs(root.left,2*i+1,n) and self.dfs(root.right,2*i+2,n)
        
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        #return self.bfs(root)
        n=self.count(root)
        return self.dfs(root,0,n)