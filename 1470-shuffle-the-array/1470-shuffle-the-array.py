class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l,r=0,n
        ans=[]
        while l<n:
            ans.append(nums[l])
            l+=1
            ans.append(nums[r])
            r+=1
        return ans