class Solution:
    def emptyDct(self, dct):
        for key in dct:
            if dct[key] > 0:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        # Dictionary of occurences of character of t that is in s
        # Two pointers
        # If full t in substring, cal res, increase i, else increase j
        dct = {}
        for i in range(len(t)):
            if t[i] in dct:
                dct[t[i]] += 1
            else:
                dct[t[i]] = 1
        
        res = s + "a"
        i = 0
        j = 0
        if len(t) > len(s) or t == "":
            return ""
        if s[0] in dct:
            dct[s[0]] -= 1

        while i <= j and j < len(s):
            if self.emptyDct(dct):
                if j - i + 1 < len(res):
                    res = s[i: j + 1]
                if s[i] in dct:
                    dct[s[i]] += 1
                i += 1
            else:
                j += 1
                if j < len(s) and s[j] in dct:
                    dct[s[j]] -= 1

        return res if len(res) <= len(s) else ""
