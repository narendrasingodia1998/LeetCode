class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        dict1=collections.defaultdict(int)
        dict2=collections.defaultdict(int)
        for i in p:
            dict1[i]+=1
        j=0
        ans=[]
        for i,char in enumerate(s):
            dict2[char]+=1
            if i>=len(p)-1:
                if dict1==dict2:
                    ans.append(j)
                dict2[s[j]]-=1
                if not dict2[s[j]]:
                    del dict2[s[j]]
                j+=1
        return ans