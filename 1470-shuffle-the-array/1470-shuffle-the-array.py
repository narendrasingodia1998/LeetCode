class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l=0
        ans=[]
        while l<n:
            ans.append(nums[l])
            ans.append(nums[l+n])
            l+=1
        return ans