#User function Template for python3

class Solution:
    def endPoints(self, matrix, R, C):
        #code here
        #    Right  down   left    up
        dir=[(0,1),(1,0),(0,-1),(-1,0)]
        def solve(row,col,c_dir):
            dr,dc=dir[c_dir%4]
            if row<0 or row>=R or col<0 or col>=C:
                #r and c is out range
                return row-dr,col-dc
            if matrix[row][col]==1:
                c_dir+=1
                dr,dc=dir[c_dir%4]
                matrix[row][col]=0
            row+=dr
            col+=dc
            return solve(row,col,c_dir)
        return solve(0,0,0)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().strip().split())
        matrix = []
        for i in range(r):
            line = [int(x) for x in input().strip().split()]
            matrix.append(line)
        ob = Solution()
        ans = ob.endPoints(matrix,r,c)
        print('(',ans[0],', ',ans[1],')',sep ='')

# } Driver Code Ends