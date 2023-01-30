class Solution:
    def tribonacci(self, n: int) -> int:
        if n==0:
            return 0
        elif n==1 or n==2:
            return 1
        third_last=0
        second_last=last=1
        ans=0
        while n>2:
            ans=last+second_last+third_last
            last,second_last,third_last=ans,last,second_last
            n-=1
        return ans
            