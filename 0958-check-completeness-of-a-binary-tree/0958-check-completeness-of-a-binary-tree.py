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
    
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        return self.bfs(root)