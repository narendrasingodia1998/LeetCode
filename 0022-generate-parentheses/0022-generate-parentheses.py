class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=set()
        cur=""
        def backtrack(n,curr):
            if n==0:
                res.add(curr)
                return 
            for i in range(len(curr)):
                backtrack(n-1,curr[:i]+'()'+curr[i:])
            backtrack(n-1,curr+'()')
        backtrack(n,"")
        return res