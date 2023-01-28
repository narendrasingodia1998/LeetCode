class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count={}
        for i in s:
            if i not in count:
                count[i]=0
            count[i]+=1
        for i in t:
            if i not in count or count[i]==0:
                return False
            count[i]-=1
        for i in count.values():
            if i:
                return False
        return True