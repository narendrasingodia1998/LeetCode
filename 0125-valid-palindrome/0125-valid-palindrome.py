class Solution:
    def alphanumeric(self,s):
        return ('a'<=s<='z') or ('0'<=s<='9')
    
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        i,j,n=0,len(s)-1,len(s)
        while i<j:
            #setting i non_alphanumeric Character
            while (i<n and not self.alphanumeric(s[i])):
                i+=1
            while (j>=0 and not self.alphanumeric(s[j])):
                j-=1
            if i<j and s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True
            