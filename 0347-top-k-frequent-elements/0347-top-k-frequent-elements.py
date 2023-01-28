class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        for i in nums:
            if i not in hashmap:
                hashmap[i]=0
            hashmap[i]+=1
        ans=[(val,key) for key,val in hashmap.items()]
        ans.sort()
        res=[]
        for i in ans[-k:]:
            res.append(i[1])
        return res