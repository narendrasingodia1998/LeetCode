class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic={char:i for i,char in enumerate(order)}
        return words==sorted(words,key=lambda x:tuple(dic[i] for i in x))