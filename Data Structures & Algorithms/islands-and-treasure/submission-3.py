class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        res = 0
        rows = len(grid)
        cols = len(grid[0])
        INF = 2 ** 31 - 1
        stack = []
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    stack.append([i, j])
        # BFS
        while stack:
            new_stack = []
            for x, y in stack:
                for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == INF:
                        grid[nx][ny] = grid[x][y] + 1
                        new_stack.append([nx, ny])
            stack = new_stack
        return