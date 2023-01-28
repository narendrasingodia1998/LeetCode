class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        n=len(nums)
        left_prod=[1]*n
        right_prod=[1]*n
        for i in range(1,n):
            left_prod[i]=left_prod[i-1]*nums[i-1]
        for i in range(n-2,-1,-1):
            right_prod[i]=right_prod[i+1]*nums[i+1]
        res=[a*b for a,b in zip(left_prod,right_prod)]
        return res
        """
        n=len(nums)
        res=[1]*n
        prefix=1
        for i,val in enumerate(nums):
            res[i]=prefix
            prefix*=nums[i]
        postfix=1
        for i in range(n-1,-1,-1):
            res[i]*=postfix
            postfix*=nums[i]
        return res
            