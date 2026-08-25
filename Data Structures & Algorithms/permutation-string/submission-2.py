class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        s1Dct = {}
        for c in s1:
            if c in s1Dct:
                s1Dct[c] += 1
            else:
                s1Dct[c] = 1
        slidingWindow = s1[:len(s1)]
        # Initial check
        for i in range(len(s1)):
            if s2[i] in s1Dct:
                s1Dct[s2[i]] = s1Dct[s2[i]] - 1

        def checkDct():
            for c in s1Dct:
                if s1Dct[c] != 0:
                    return False
            return True
        
        if checkDct():
            return True

        # Loop
        i = 0
        while i < len(s2) - len(s1):
            i += 1
            if s2[i - 1] in s1Dct:
                s1Dct[s2[i - 1]] += 1
            if s2[i + len(s1) - 1] in s1Dct:
                s1Dct[s2[i + len(s1) - 1]] -= 1
            # Check
            if checkDct():
                return True
        return False
        