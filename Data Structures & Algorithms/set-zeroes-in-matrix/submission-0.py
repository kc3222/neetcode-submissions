class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        zeros = set()
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zeros.add((i, j))
        for i, j in zeros:
            # Rows
            for t in range(cols):
                matrix[i][t] = 0
            # Cols
            for t in range(rows):
                matrix[t][j] = 0