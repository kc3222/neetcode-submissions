class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        res = 1
        i = 0
        j = 1
        curr_set = set(s[0])
        while j < len(s):
            if s[j] in curr_set:
                i += 1
                curr_set.remove(s[i - 1])
            else:
                if j - i + 1 > res:
                    res = j - i + 1
                curr_set.add(s[j])
                j += 1
        return res
