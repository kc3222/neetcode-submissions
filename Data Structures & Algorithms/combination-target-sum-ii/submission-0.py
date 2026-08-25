class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidateDct = defaultdict(int)
        for candidate in candidates:
            candidateDct[candidate] += 1
        candidateSet = list(set(candidates))
        
        def backTrack(i, curr, currSum):
            if currSum == target:
                res.append(curr[:])
            if currSum > target:
                return 
            for c in range(i, len(candidateSet)):
                candidate = candidateSet[c]
                for o in range(1, candidateDct[candidate] + 1):
                    curr.extend([candidate for _ in range(o)])
                    currSum += candidate * o
                    backTrack(c + 1, curr, currSum)
                    for _ in range(1, o + 1):
                        curr.pop()
                    currSum -= candidate * o
            return 
        
        backTrack(0, [], 0)
        return res