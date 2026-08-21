class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        # Find the row
        def searchRow(low, high):
            if matrix[high][0] <= target:
                return high
            middle = (low + high) // 2
            while low < middle:
                if matrix[middle][0] == target:
                    return middle
                elif matrix[middle][0] > target:
                    high = middle
                else:
                    low = middle
                middle = (low + high) // 2
            return low
        rowIdx = searchRow(0, rows - 1)
        row = matrix[rowIdx]
        # Find the col
        def searchCol(low, high):
            middle = (low + high) // 2
            while low < middle:
                if row[middle] == target:
                    return middle
                elif row[middle] > target:
                    high = middle
                else:
                    low = middle
                middle = (low + high) // 2
            if row[low] == target:
                return low
            elif row[high] == target:
                return high
            return -1
        return True if searchCol(0, cols - 1) != -1 else False