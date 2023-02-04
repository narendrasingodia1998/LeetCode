#import collections
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
            dict1=collections.defaultdict(int)
            dict2=collections.defaultdict(int)
            if len(s1)>len(s2):
                return False
            for i in s1:
                dict1[i]+=1
            j=0
            for i,char in enumerate(s2):
                dict2[char]+=1
                if i>=len(s1)-1:
                    if dict1==dict2:
                        return True
                    dict2[s2[j]]-=1
                    if not dict2[s2[j]]:
                        del dict2[s2[j]]
                    j+=1
            return False