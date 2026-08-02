class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort each str
        dct = {}
        for i in range(len(strs)):
            sorted_str = ''.join(sorted(strs[i]))
            if sorted_str in dct:
                dct[sorted_str].append(strs[i])
            else:
                dct[sorted_str] = [strs[i]]
        res = []
        for key in dct:
            res.append(dct[key])
        return res