class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
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
        """
        hashmap={}
        freq=[[] for i in range(len(nums)+1)]
        for i in nums:
            if i not in hashmap:
                hashmap[i]=0
            hashmap[i]+=1
        for key,val in hashmap.items():
            freq[val].append(key)
        res=[]
        for i in range(len(freq)-1,0,-1):
            for j in freq[i]:
                res.append(j)
                if len(res)==k:
                    return res
        
        