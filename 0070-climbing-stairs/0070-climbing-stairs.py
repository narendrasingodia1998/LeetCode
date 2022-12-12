class Solution:
    def climbStairs(self, n: int) -> int:
        if(n==1):
            return 1
        second_last_step=1
        last_step=2
        curr=last_step
        for i in range(3,n+1):
            curr=last_step+second_last_step
            second_last_step=last_step
            last_step=curr
        return last_step
        