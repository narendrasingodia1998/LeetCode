class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        wordMap=collections.defaultdict(set)
        for word in ideas:
            wordMap[word[0]].add(word[1:])
        
        ans=0
        for char1 in wordMap:
            for char2 in wordMap:
                if char1==char2:
                    continue
                intersection=0
                for suffix in wordMap[char1]:
                    if suffix in wordMap[char2]:
                        intersection+=1
                
                distinct1=len(wordMap[char1])-intersection
                distinct2=len(wordMap[char2])-intersection
                ans+=distinct1*distinct2
        return ans