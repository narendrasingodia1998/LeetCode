class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r=0,sum(weights)
        ans=0
        
        def isPossible(capacity):
            load=0
            total_days=1
            for i in weights:
                if load+i<=capacity:
                    load+=i
                elif i>capacity:
                    return False
                else:
                    total_days+=1
                    load=i
            #print(f"Capacity :{capacity} {total_days<=days}")
            return total_days<=days
        
        
        while l<=r:
            mid=(l+r)//2
            if isPossible(mid):
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans