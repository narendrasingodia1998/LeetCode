class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        dict1=defaultdict(int)
        l=r=0
        n=len(fruits)
        ans=0
        while r<n:
            dict1[fruits[r]]+=1
            while len(dict1)>2:
                dict1[fruits[l]]-=1
                if not dict1[fruits[l]]:
                    del dict1[fruits[l]]
                l+=1
            ans=max(ans,r-l+1)
            r+=1
        return ans