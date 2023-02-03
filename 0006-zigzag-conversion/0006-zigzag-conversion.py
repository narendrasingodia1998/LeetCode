class Solution:
    def convert(self, s: str, numRows: int) -> str:
            i=0
            j=len
            if numRows==1:
                return s
            ans=["" for _ in range(numRows)]
            flag=True #increasing 
            for char in s:
                if flag:
                    ans[i]+=char
                    i+=1
                    if i==numRows:
                        i=numRows-2
                        flag=False
                else:
                    ans[i]+=char
                    i-=1    
                    if i==-1:
                        i=1
                        flag=True
            return "".join(ans)