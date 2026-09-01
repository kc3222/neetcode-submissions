class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # Search for regions
        # DFS to see if the region touches the edge
        rows = len(board)
        cols = len(board[0])
        visited = set()

        def dfs(x, y):
            stack = [(x, y)]
            visiting = [(x, y)]
            visited.add((x, y))
            surrounded = True
            while stack:
                cx, cy = stack.pop()
                if cx == 0 or cx == rows - 1 or cy == 0 or cy == cols - 1:
                    surrounded = False
                for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < rows and 0 <= ny < cols and board[nx][ny] == "O" and (nx, ny) not in visited:
                        stack.append((nx, ny))
                        visiting.append([nx, ny])
                        visited.add((nx, ny))
            return surrounded, visiting

        for i in range(1, rows):
            for j in range(1, cols):
                if board[i][j] == "O" and (i, j) not in visited:
                    surrounded, v = dfs(i, j)
                    if surrounded:
                        for x, y in v:
                            board[x][y] = "X"