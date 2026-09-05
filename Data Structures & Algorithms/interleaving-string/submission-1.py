class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dct = {}
        if len(s3) != len(s1) + len(s2):
            return False

        def dp(i, j):
            if i == len(s1):
                if s2[j:] == s3[i + j: ]:
                    return True
                return False
            if j == len(s2):
                if s1[i:] == s3[i + j: ]:
                    return True
                return False
            
            if (i, j) in dct:
                return dct[(i, j)]

            if s1[i] == s3[i + j]:
                if dp(i + 1, j):
                    dct[(i, j)] = True
                    return True
            if s2[j] == s3[i + j]:
                if dp(i, j + 1):
                    dct[(i, j)] = True
                    return True
            dct[(i, j)] = False
            return False
        return dp(0, 0)