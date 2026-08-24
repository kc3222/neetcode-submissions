class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == "":
            return 0
        if len(s) == 1:
            return s
        res = s[0]
        if s[0] == s[1]:
            res = s[0: 2]
        # Character center or two chacters similar
        for i in range(1, len(s) - 1):
            # Character center
            if s[i - 1] == s[i + 1]:
                # Find longest palindrome
                j = 1
                while i - j >= 0 and i + j < len(s) and s[i - j] == s[i + j]:
                    j += 1
                j -= 1
                if 2 * j + 1 > len(res):
                    res = s[i - j: i + j + 1]
            if s[i] == s[i + 1]:
                # Find longest palidrome
                j = 1
                while i - j + 1 >= 0 and i + j < len(s) and s[i - j + 1] == s[i + j]:
                    j += 1
                j -= 1
                if 2 * j > len(res):
                    res = s[i - j + 1: i + j + 1]
        return res