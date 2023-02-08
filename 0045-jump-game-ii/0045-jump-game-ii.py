class Solution:
    def dp_solution(self,nums):
        n=len(nums)
        dp=[0]*n
        #dp[i] means minimum number of jump to reach ith index
        for i in range(1,n):
            ans=1e4+1
            for j in range(i):
                if j+nums[j]>=i:
                    ans=min(ans,dp[j]+1)
            dp[i]=ans
        return dp[-1]
    
    def jump(self, nums: List[int]) -> int:
        res=0
        l=r=0
        
        while r<len(nums)-1:
            far_most=0
            for i in range(l,r+1):
                far_most=max(far_most,i+nums[i])
            res+=1
            l=r+1
            r=far_most
        return res
        