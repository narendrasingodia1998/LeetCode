class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        i,j,n=0,len(s)-1,len(s)
        while i<j:
            #setting i non_alphanumeric Character
            while (i<n and 
                  not ((s[i]>='a' and s[i]<='z') or 
                    (s[i]>='0' and s[i]<='9'))):
                i+=1
            while (j>=0 and 
                 not  ((s[j]>='a' and s[j]<='z') or 
                    (s[j]>='0' and s[j]<='9'))):
                j-=1
            if i<j and s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True
            