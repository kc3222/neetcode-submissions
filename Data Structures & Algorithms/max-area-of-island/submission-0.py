class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        visited = set()
        rows = len(grid)
        cols = len(grid[0])

        def dfs(x, y):
            visited.add((x, y))
            curr = 1
            for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                if 0 <= x + dx < rows and 0 <= y + dy < cols and grid[x + dx][y + dy] == 1 and (x + dx, y + dy) not in visited:
                    curr += dfs(x + dx, y + dy)
            return curr

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visited:
                    res = max(res, dfs(i, j))
        return res