class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
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
        