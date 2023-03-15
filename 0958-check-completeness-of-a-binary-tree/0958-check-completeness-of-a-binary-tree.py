# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue=deque()
        last_index=-1
        queue.append((root,0))
        while len(queue):
            size=len(queue)
            for i in range(size):
                node,index=queue.popleft()
                if index-last_index!=1:
                    return False
                last_index=index
                if node.left:
                    queue.append((node.left,2*index+1))
                if node.right:
                    queue.append((node.right,2*index+2))
        return True