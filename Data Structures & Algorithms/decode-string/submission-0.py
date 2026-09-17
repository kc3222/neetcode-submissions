class Solution:
    def decodeString(self, s: str) -> str:
        numChar = [str(i) for i in range(10)]
        def helper(s, i):
            curr = ""
            num = ""
            while i < len(s):
                if s[i] == "[":
                    insideStr, i = helper(s, i + 1)
                    for j in range(int(num)):
                        curr += insideStr
                    num = ""
                elif s[i] == "]":
                    return curr, i
                elif s[i] in numChar:
                    num += s[i]
                else:
                    curr += s[i]
                i += 1
            return curr
        return helper(s, 0)
