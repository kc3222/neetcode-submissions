class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        mat = [[0 for i in range(cols)] for j in range(rows)]
        res = 1

        def dp(x, y):
            if mat[x][y] != 0:
                return mat[x][y]
            maxPath = 0
            for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < rows and 0 <= ny < cols and matrix[nx][ny] > matrix[x][y]:
                    maxPath = max(maxPath, dp(nx, ny))
            mat[x][y] = 1 + maxPath
            return mat[x][y]

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    res = max(res, dp(i, j))
        return res
