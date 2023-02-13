class Solution:
    def countOdds(self, low: int, high: int) -> int:
        no_element=high-low+1
        if no_element%2==0:
            return no_element//2
        if low%2==0:
            return no_element//2
        return no_element//2+1