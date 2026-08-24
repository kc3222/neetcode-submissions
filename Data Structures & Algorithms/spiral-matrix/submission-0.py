class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        m, n = len(matrix), len(matrix[0])
        offset = 0
        # loop while the band still has >= 1 row AND >= 1 col left
        while offset < m - offset and offset < n - offset:
            # Top
            for i in range(offset, n - offset):
                res.append(matrix[offset][i])
            # Right
            for i in range(offset + 1, m - offset):
                res.append(matrix[i][n - offset - 1])
            # Bottom - only if the bottom row isn't the top row
            if m - offset - 1 > offset:  
                for i in range(n - offset - 2, offset - 1, -1):
                    res.append(matrix[m - offset - 1][i])
            # Left — only if the left col isn't the right col
            if n - offset - 1 > offset: 
                for i in range(m - offset - 2, offset, -1):
                    res.append(matrix[i][offset])
            offset += 1
        return res