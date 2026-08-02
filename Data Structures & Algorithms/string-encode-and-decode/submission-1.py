class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += i
            res += "."
        return res

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        res = s.split(".")
        res.pop()
        return res
