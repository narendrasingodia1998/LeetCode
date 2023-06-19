class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        height,ans = 0,0
        for i in gain:
            height += i
            ans = max(ans,height)
        return ans