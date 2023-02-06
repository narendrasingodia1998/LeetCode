class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #dp[i][j] is number of ways to reach to finish line 
        dp=[[0]*n for _ in range(m) ]
        #Base conditions 
        for i in range(n):
            dp[m-1][i]=1
        for i in range(m):
            dp[i][n-1]=1
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                dp[i][j]=dp[i][j+1]+dp[i+1][j]
        return dp[0][0]