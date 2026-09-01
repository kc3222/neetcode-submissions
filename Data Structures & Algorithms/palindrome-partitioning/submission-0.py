class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)

        def palidrome(x):
            for i in range(len(x)):
                if x[i] != x[len(x) - 1 - i]:
                    return False
            return True
        
        def backTrack(j, curr):
            if j == n:
                res.append(curr[:])
                return 

            for i in range(j, n):
                if palidrome(s[j: i + 1]):
                    curr.append(s[j: i + 1])
                    backTrack(i + 1, curr)
                    curr.pop()
            return

        backTrack(0, [])

        return res