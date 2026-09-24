class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        def dfs(x, y):
            # Out of bounds or water: this side is a border edge
            if x < 0 or x >= rows or y < 0 or y >= cols or grid[x][y] == 0:
                return 1
            # Already-visited land: shared edge, contributes nothing
            if (x, y) in visited:
                return 0
            visited.add((x, y))
            res = 0
            # Unvisited land: recurse and collect the border edges from all 4 sides
            for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                res += dfs(x + dx, y + dy)
            return res

        # Exactly one island, so start DFS from the first land cell found
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 1:
                    return dfs(x, y)
        return 0