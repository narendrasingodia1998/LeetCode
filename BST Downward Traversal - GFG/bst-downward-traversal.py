#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

'''
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
'''

class Solution:
    def solve(self,root,x):
        ans=0
        if not root:
            return ans
        if x==0:
            ans=root.data
        ans+=self.solve(root.left,x-1)
        ans+=self.solve(root.right,x+1)
        return ans
        
    def verticallyDownBST(self, root, target):
        temp=root
        ans=-1
        while temp:
            if temp.data==target:
                ans=self.solve(temp,0)
                ans-=temp.data
                return ans
            elif temp.data>target:
                temp=temp.left
            else:
                temp=temp.right
        return ans
        #code here

#{ 
 # Driver Code Starts.

from collections import defaultdict
from collections import deque
from sys import stdin, stdout
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root

if __name__ == '__main__':
    test_cases = int(input())
    for _ in range (test_cases):
        target = int(input())
        N = input()
        root = buildTree(N)
        res = Solution().verticallyDownBST(root, target)
        print(res)
# } Driver Code Ends