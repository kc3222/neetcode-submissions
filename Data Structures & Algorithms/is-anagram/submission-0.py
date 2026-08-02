class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dct = defaultdict(int)
        for i in range(len(s)):
            s_dct[s[i]] += 1
            s_dct[t[i]] -= 1
        for key in s_dct:
            if s_dct[key] != 0:
                return False
        return True
