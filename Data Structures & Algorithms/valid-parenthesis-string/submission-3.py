class Solution:
    def checkValidString(self, s: str) -> bool:
        memo = {}
        # DP with memo
        def dp(i, openCounter):
            if (i, openCounter) in memo:
                return memo[(i, openCounter)]
            if i == len(s):
                if openCounter != 0:
                    return False
                return True
            if s[i] == '(':
                memo[(i, openCounter)] = dp(i + 1, openCounter + 1)
            elif s[i] == ')':
                if openCounter - 1 < 0:
                    memo[(i, openCounter)] = False
                else:
                    memo[(i, openCounter)] =  dp(i + 1, openCounter - 1)
            else:
                memo[(i, openCounter)] = dp(i + 1, openCounter + 1) or dp(i + 1, max(openCounter - 1, 0)) or dp(i + 1, openCounter)
            return memo[(i, openCounter)]
            
        return dp(0, 0)