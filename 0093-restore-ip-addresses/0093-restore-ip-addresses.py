class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res=[]
        if len(s)>12:
            return res
        
        def backtrack(i,dot,currIp):
            if i==len(s) and dot==4:
                res.append(currIp[:-1])
                return 
            if dot>4:
                return
            for j in range(i,min(i+3,len(s))):
                if int(s[i:j+1])<=255 and (i == j or s[i]!='0'):
                    backtrack(j+1,dot+1,currIp+s[i:j+1]+'.')
        backtrack(0,0,"")
        return res