class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict={}
        for i,val in enumerate(nums):
            if val in dict:
                if i-dict[val]<=k:
                    return True
            dict[val]=i
        return False
            
        