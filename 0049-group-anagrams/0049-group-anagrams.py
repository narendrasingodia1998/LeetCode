class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap={}
        for i in strs:
            val="".join(sorted(i))
            if val not in hashmap:
                hashmap[val]=[]
            hashmap[val].append(i)
        ans=[val for val in hashmap.values()]
        return ans
        