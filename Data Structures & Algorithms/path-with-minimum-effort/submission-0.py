class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # Heap (effort, currX, currY)
        rows = len(heights)
        cols = len(heights[0])
        visited = [[float('inf') for j in range(cols)] for i in range(rows)]
        heap = []
        heapq.heappush(heap, (0, 0, 0))
        
        while heap:
            effort, x, y = heapq.heappop(heap)
            # Result
            if x == rows - 1 and y == cols - 1:
                return effort
            for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    # Check if this is a better path
                    neffort = max(abs(heights[nx][ny] - heights[x][y]), effort)
                    if neffort < visited[nx][ny]:
                        visited[nx][ny] = neffort
                        heapq.heappush(heap, (neffort, nx, ny))
        
        return heights[-1][-1]