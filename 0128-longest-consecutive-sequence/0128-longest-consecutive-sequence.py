class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset=set(nums)
        longest=0
        for val in nums:
            if val-1 not in hashset:
                length=1
                while val+length in hashset:
                    length+=1
                longest=max(longest,length)
        return longest