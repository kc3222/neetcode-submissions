class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if s == "":
            return 0
        if len(s) == 1:
            return 1
        dct = defaultdict(int)
        dct[s[0]] = 1
        i = 0
        j = 0
        res = 1
        while j < len(s):
            max_value = max(list(dct.values()))
            if k < (j - i + 1) - max_value:
                dct[s[i]] -= 1
                i += 1
            else:
                if res < (j - i + 1):
                    res = j - i + 1
                j += 1
                if j < len(s):
                    dct[s[j]] += 1
        return res
