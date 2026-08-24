class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dct = {}

        def dp(x, y):
            if (x, y) in dct:
                return dct[(x, y)]
            if x == len(text1):
                return 0
            if y == len(text2):
                return 0
            if text1[x] == text2[y]:
                dct[(x, y)] = dp(x + 1, y + 1) + 1
            else:
                right = dp(x + 1, y)
                left = dp(x, y + 1)
                dct[(x, y)] = max(left, right)
            return dct[(x, y)]
        
        return dp(0, 0)