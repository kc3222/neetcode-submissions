class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        # Track top most row separately
        topRow = False
        for j in range(cols):
            if matrix[0][j] == 0:
                topRow = True
        # Mark rows and columns to turn to 0
        for i in range(1, rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        # Change
        for i in range(1, rows):
            if matrix[i][0] == 0:
                for j in range(cols):
                    matrix[i][j] = 0
        for j in range(cols):
            if matrix[0][j] == 0:
                for i in range(1, rows):
                    matrix[i][j] = 0
        if topRow:
            for j in range(cols):
                matrix[0][j] = 0