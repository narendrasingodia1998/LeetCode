class Solution:
    def dp(self,grid):
        m,n=len(grid),len(grid[0])
        
        dp1=[[0]*(n+1) for _ in range(m+1)]
        #dp1[i][j] means number of path to reach location (i-1,j-1) from (0,0)
        dp1[1][1]=1
        for i in range(1,m+1):
            for j in range(1,n+1):
                if grid[i-1][j-1]:
                    dp1[i][j]+=dp1[i-1][j]+dp1[i][j-1]
                
        dp2=[[0]*(n+1) for _ in range(m+1)]
        #dp2[i][j] means number of path to reach loaction (i,j) from (m-1,n-1)
        dp2[m-1][n-1]=1
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if grid[i][j]:
                    dp2[i][j]+=dp2[i+1][j]+dp2[i][j+1]
        
        target=dp1[m][n]
        for i in range(m):
            for j in range(n):
                if not((i==0 and j==0) or (i==m-1 and j==n-1)):
                    if dp1[i+1][j+1]*dp2[i][j]==target:
                        return True
        return False
    
    def dfs(self,grid,i,j) ->bool:
        m,n=len(grid),len(grid[0])
        if i>=m or j>=n or not grid[i][j]:
            return False
        if i==m-1 and j==n-1:
            return True
        grid[i][j]=0
        return self.dfs(grid,i+1,j) or self.dfs(grid,i,j+1)
    
    def two_dfs(self,grid):
        if not self.dfs(grid,0,0):
            return True
        grid[0][0]=1
        return not self.dfs(grid,0,0)
            
        
        
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        #return self.dp(grid)        
        return self.two_dfs(grid)