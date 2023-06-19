class Solution:
    def countPaths(self, grid) -> int:  
        m,n = len(grid),len(grid[0])
        mod = 1e9+7
        dp = [[-1]*n for i in range(m)]
        def solve(i,j,last):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j]<=last:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            right = solve(i,j+1,grid[i][j])
            left = solve(i,j-1,grid[i][j])
            up = solve(i-1,j,grid[i][j])
            down = solve(i+1,j,grid[i][j])
            dp[i][j] = (1+right+left+up+down)%mod
            return dp[i][j]
        
        for i in range(m):
            for j in range(n):
                if dp[i][j] == -1:
                    solve(i,j,-1)
        ans = 0
        
        for i in range(m):
            for j in range(n):
                ans += dp[i][j]
        return int(ans%mod)