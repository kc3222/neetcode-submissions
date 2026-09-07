class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0
        memo = {}
        def dp(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            res = dp(i + 1, j)
            if s[i] == t[j]:
                res += dp(i + 1, j + 1)
            memo[(i, j)] = res
            return memo[(i, j)]
        
        res = dp(0, 0)
        return res