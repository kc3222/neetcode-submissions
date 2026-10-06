class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # Trust dict
        trustDct = defaultdict(int)
        trusteeDct = defaultdict(int)
        for t in trust:
            a, b = t
            trustDct[b] += 1
            trusteeDct[a] += 1
        for p in trustDct:
            if trustDct[p] == n - 1:
                if trusteeDct[p] == 0:
                    return p
        return -1