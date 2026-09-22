class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        res = [False for i in range(len(s))]
        if s[0] == '1':
            return False
        res[0] = True
        trueCount = 0
        for i in range(minJump, len(s)):
            if i >= minJump:
                # right edge: index (i - minJump) just entered the window.
                trueCount += res[i - minJump]
            if i - maxJump - 1 >= 0:
                # left edge: index (i - maxJump - 1) just fell out of the window.
                trueCount -= res[i - maxJump - 1]
            if s[i] == '0' and trueCount > 0:
                res[i] = True
        return res[-1]