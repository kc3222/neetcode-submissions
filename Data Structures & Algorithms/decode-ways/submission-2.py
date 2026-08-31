class Solution:
    def getDecodedChar(self, s: str):
        if s[0] == "0" or int(s) > 26:
            return False
        return True

    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if s[0] == "0":
            return 0
        if len(s) == 1:
            return 1
        res = [0 for i in range(len(s))]
        res[0] = 1 if s[0] != "0" else 0
        res[1] = 1 if s[1] != "0" else 0
        if self.getDecodedChar(s[:2]):
            res[1] += 1
        for i in range(2, len(s)):
            if self.getDecodedChar(s[i]):
                res[i] += res[i - 1]
            if self.getDecodedChar(s[i - 1: i + 1]):
                res[i] += res[i - 2]
        return res[-1]