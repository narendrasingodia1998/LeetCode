class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans=[]
        def valid_panl(s):
            return s==s[::-1]
        def backtrack(index,curr):
            if index==len(s):
                #print(index," ",curr)
                ans.append(curr[:])
                #print(ans)
                return 
            for i in range(index,len(s)):
                if valid_panl(s[index:i+1]):
                    curr.append(s[index:i+1])
                    #print(index," ",i+1," ",curr)
                    backtrack(i+1,curr)
                    curr.pop()
        a=[]
        backtrack(0,a)
        return ans