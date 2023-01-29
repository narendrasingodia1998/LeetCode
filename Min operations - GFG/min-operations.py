class Solution:
    def solve(self, a : int, b : int) -> int:
        # code here
        if a==b:
            return 0
        x=a&b
        if a&x==b or b&x==a:
            return 1
        return 2



#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a = int(input())
        
        
        b = int(input())
        
        obj = Solution()
        res = obj.solve(a, b)
        
        print(res)
        

# } Driver Code Ends