class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        rottenFruits = []
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    rottenFruits.append([i, j])
        # BFS
        res = -1
        while rottenFruits:
            res += 1
            newRottens = []
            for x, y in rottenFruits:
                for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        newRottens.append([nx, ny])
            rottenFruits = newRottens
        # Check if all fruits are rotten
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1
        return res if res > -1 else 0