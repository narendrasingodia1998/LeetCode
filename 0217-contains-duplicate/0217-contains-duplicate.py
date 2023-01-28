class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict={}
        for i in nums:
            if i in dict:
                return True
            dict[i]=1
        return False
        """
        hashset=set()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False
        """