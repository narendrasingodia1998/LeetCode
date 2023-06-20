class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        running_sum = [0]
        ans = []
        for num in nums:
            running_sum.append(running_sum[-1]+num)
        for i in range(len(nums)):
            left_idx = i-k
            right_idx = i+k+1
            if left_idx<0 or right_idx>=len(running_sum):
                ans.append(-1)
            else:
                ans.append((running_sum[right_idx]-running_sum[left_idx])//(2*k+1))
        return ans
        