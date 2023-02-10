class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n=len(grid)
        queue =collections.deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    queue.append((i,j))
        
        if len(queue)==0 or len(queue)==n**2:
            return -1
        
        level=-1
        dir_=[(-1,0),(0,1),(0,1),(1,0),(0,-1)]
        while queue:
            size=len(queue)
            #print(queue)
            for i in range(size):
                i,j=queue.popleft()
                for di,dj in dir_:
                    new_i=i+di
                    new_j=j+dj
                    if new_i<0 or new_i>=n or new_j<0 or new_j>=n or grid[new_i][new_j]:
                        continue
                    grid[new_i][new_j]=1
                    queue.append((new_i,new_j))
            level+=1
        return level
                
        