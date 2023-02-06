class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        cache=[[-1]*n for _ in range(m)]
        cache[m-1][n-1]=1
        def solve(x,y):
            if x<0 or x>=m or y<0 or y>=n or obstacleGrid[x][y]:
                return 0
            if not cache[x][y]==-1:
                return cache[x][y]
            cache[x][y]=solve(x+1,y)+solve(x,y+1)
            return cache[x][y]
        return solve(0,0)