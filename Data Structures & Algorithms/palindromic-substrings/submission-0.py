class Solution:
    def countSubstrings(self, s: str) -> int:
        # Greedy count
        length = len(s)
        res = 0
        for i in range(len(s)):
            j = 0
            while 0 <= i - j and i + j + 1 < length and s[i - j] == s[i + j + 1]: # aa
                res += 1
                j += 1
            j = 0
            while 0 <= i - j and i + j < length and s[i - j] == s[i + j]: # asa
                res += 1
                j += 1
        return res
