class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        # Backtrack
        def backtrack(curr, j):
            if len(curr) == k:
                res.append(curr[:])
            for i in range(j, n + 1):
                curr.append(i)
                backtrack(curr, i + 1)
                curr.pop()
        
        backtrack([], 1)
        return res