class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        res = [False for i in range(len(s))]
        if s[0] == '1':
            return False
        res[0] = True
        for i in range(minJump, len(s)):
            if s[i] == '1':
                continue
            for j in range(minJump, maxJump + 1):
                if 0 <= i - j and res[i - j]:
                    res[i] = True
                    break
        return res[-1]