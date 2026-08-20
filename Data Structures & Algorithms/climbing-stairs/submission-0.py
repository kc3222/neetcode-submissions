class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [1 for i in range(n + 1)]
        for i in range(2, n + 1):
            arr[i] = arr[i - 1] + arr[i - 2]
        return arr[n]
