class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = [i for i in range(len(s))]
        dct = {}
        for i in range(len(s)):
            if s[i] not in dct:
                dct[s[i]] = i
            else:
                j = dct[s[i]]
                for x in range(j, i + 1):
                    res[x] = res[j]

        r = []
        curr = 0
        for i in range(1, len(res)):
            if res[i] == res[i - 1]:
                i += 1
            else:
                r.append(i - curr)
                curr = i
        if curr == len(res) - 1:
            r.append(1)
        else:
            r.append(len(res) - curr)
        return r