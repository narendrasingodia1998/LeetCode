class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        ans=[]
        i=len(num)-1
        carry=0
        while i>=0 or carry or k:
            sum_=carry+k%10
            if i>=0:
                sum_+=num[i]
                i-=1
            carry=sum_//10
            ans.append(sum_%10)
            k=k//10
            
        return ans[::-1]
            
            