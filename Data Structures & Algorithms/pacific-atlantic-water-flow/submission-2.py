class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # DFS
        # Pacific board and Atlantic board
        rows = len(heights)
        cols = len(heights[0])
        # DFS
        def dfs(x, y, visited):
            visited.add((x, y))
            if x == 0 and y == cols - 1:
                return True, True
            if x == rows - 1 and y == 0:
                return True, True
            # loop
            pacific, atlantic = False, False
            if x == 0 or y == 0:
                pacific, atlantic = True, False
            if x == rows - 1 or y == cols - 1:
                pacific, atlantic = False, True
            for dx, dy in [[1, 0], [-1 , 0], [0, 1], [0, -1]]:
                if 0 <= x + dx < rows and 0 <= y + dy < cols and (x + dx, y + dy) not in visited:
                    if heights[x][y] >= heights[x + dx][y + dy]:
                        p, a = dfs(x + dx, y + dy, visited)
                        pacific = p if p else pacific
                        atlantic = a if a else atlantic
            return pacific, atlantic

        res = []
        for i in range(rows):
            for j in range(cols):
                visited = set()
                pacific, atlantic = dfs(i, j, visited)
                if pacific and atlantic:
                    res.append([i, j])
        return res