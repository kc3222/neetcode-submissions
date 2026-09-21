class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # DP
        rows = len(grid)
        cols = len(grid[0])
        dp = [[grid[i][j] for j in range(cols)] for i in range(rows)]
        for i in range(1, rows):
            dp[i][0] += dp[i - 1][0]
        for i in range(1, cols):
            dp[0][i] += dp[0][i - 1]
        for i in range(1, rows):
            for j in range(1, cols):
                dp[i][j] += min(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]