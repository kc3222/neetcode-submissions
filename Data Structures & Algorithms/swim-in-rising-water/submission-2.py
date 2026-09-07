class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        res = [[float('inf') for i in range(cols)] for j in range(rows)]
        res[0][0] = grid[0][0]
        # Heap with visited
        # Dijkstra-style traversal with min pop to guarantee smallest path
        stack = []
        heapq.heappush(stack, (grid[0][0], [0, 0]))
        
        # BFS
        while stack:
            currentVal, [x, y] = heapq.heappop(stack)

            if x == rows - 1 and y == cols - 1:
                return res[x][y]

            for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < rows and 0 <= ny < cols and res[nx][ny] == float('inf'):
                    res[nx][ny] = max(currentVal, grid[nx][ny])
                    heapq.heappush(stack, (res[nx][ny], [nx, ny]))

        return res[-1][-1]