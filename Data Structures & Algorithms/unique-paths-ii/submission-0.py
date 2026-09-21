class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # DP
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        dp = [[0 for i in range(cols)] for j in range(rows)]
        for i in range(rows):
            if obstacleGrid[i][0] != 1:
                dp[i][0] = 1
            else:
                break
        for i in range(cols):
            if obstacleGrid[0][i] != 1:
                dp[0][i] = 1
            else:
                break
        # Loop
        for i in range(1, rows):
            for j in range(1, cols):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]
