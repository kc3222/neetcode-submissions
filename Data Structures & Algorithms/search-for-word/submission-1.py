class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Search for the start of the word on the board
        # Cycle:
        # Look at left, right, up, down
        # Go to an unvisited node that matches the next character
        # Mark it as repeat
        # If no character left, return True
        # Default return False
        rows = len(board)
        cols = len(board[0])
        res = False
        # Loop
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    visited = set()
                    visited.add((i, j))
                    def backTrack(idx, x, y):
                        nonlocal res
                        if idx == len(word):
                            res = True
                            return
                        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            if 0 <= x + dx < rows and 0 <= y + dy < cols:
                                if (x + dx, y + dy) not in visited and board[x + dx][y + dy] == word[idx]:
                                    visited.add((x + dx, y + dy))
                                    backTrack(idx + 1, x + dx, y + dy)
                                    visited.remove((x + dx, y + dy))
                    backTrack(1, i, j)
                    if res:
                        return True
        return False