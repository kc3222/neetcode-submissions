class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        res = [0, 1, 1]
        for i in range(3, n + 1):
            res.append(res[-1] + res[-2] + res[-3])
        return res[-1]