class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0
        rows = len(grid)
        cols = len(grid[0])

        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 1:
                    # Calculate the perimeter of the cell:
                    maxPerim = 4
                    for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                        if 0 <= x + dx < rows and 0 <= y + dy < cols and grid[x + dx][y + dy] == 1:
                            maxPerim -= 1
                    res += maxPerim
        return res