class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backTrack(open, closed, curr):
            if open > n:
                return
            if closed > open:
                return 
            if open == n and open == closed:
                res.append(curr)
            
            backTrack(open + 1, closed, curr + "(")
            backTrack(open, closed + 1, curr + ")")
            return

        backTrack(0, 0, "")

        return res