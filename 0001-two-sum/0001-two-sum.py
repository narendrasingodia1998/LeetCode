class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for i,val in enumerate(nums):
            if target-val in hashmap:
                return [i,hashmap[target-val]]
            hashmap[val]=i
        return [-1,-1]