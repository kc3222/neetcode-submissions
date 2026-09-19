class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        while len(s) - i - 1 > i:
            t = s[i]
            s[i] = s[len(s) - i - 1]
            s[len(s) - i - 1] = t
            i += 1