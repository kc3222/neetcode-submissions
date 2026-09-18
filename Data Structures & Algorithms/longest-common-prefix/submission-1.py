class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        breakLoop = False
        while not breakLoop:
            if i == len(strs[0]):
                break
            curr = strs[0][i]
            for word in strs:
                if i == len(word) or word[i] != curr:
                    breakLoop = True
            if not breakLoop:
                i += 1
        if i == 0:
            return ""
        return strs[0][:i]