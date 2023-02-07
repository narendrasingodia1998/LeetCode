class Solution:
    def method1(self,fruits):
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
    
    def method2(self,fruits):
        count=defaultdict(int)
        l=0
        for r,tree in enumerate(fruits):
            count[tree]+=1
            if len(count)>2:
                count[fruits[l]]-=1
                if not count[fruits[l]]:
                    del count[fruits[l]]
                l+=1
        return r-l+1
    
    def totalFruit(self, fruits: List[int]) -> int:
        #return self.method1(fruits)
        return self.method2(fruits)