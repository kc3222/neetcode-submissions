class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        visited = set() # set of (x, y)
        rows = len(grid)
        cols = len(grid[0])

        def dfs(x, y):
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if  -1 < x + dx < rows and -1 < y + dy < cols:
                    if grid[x + dx][y + dy] == "1" and (x + dx, y + dy) not in visited:
                        visited.add((x + dx, y + dy))
                        dfs(x + dx, y + dy)
            return

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visited:
                    res += 1
                    visited.add((i, j))
                    dfs(i, j) # Mark all lands of the island
        return res