class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Trie to create a trie of words
        # For each grid, check if it can create a word from the trie
        # Create a trie
        trie = {}
        for i, word in enumerate(words):
            curr = trie
            for c in word:
                if c in curr:
                    curr = curr[c]
                else:
                    curr[c] = {}
                    curr = curr[c]
            curr["#"] = i
        # Loop
        res = []
        rows = len(board)
        cols = len(board[0])
        visited = set()

        def dfs(x, y, dct, curr, visited):
            visited.add((x, y))
            if "#" in dct and dct["#"] != -1:
                res.append(curr)
                dct["#"] = -1
            # Keep doing dfs even after finding a word
            for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                if 0 <= x + dx < rows and 0 <= y + dy < cols:
                    if board[x + dx][y + dy] in dct and (x + dx, y + dy) not in visited:
                        dfs(x + dx, y + dy, dct[board[x + dx][y + dy]], curr + board[x + dx][y + dy], visited)
            visited.remove((x, y))
            return

        for i in range(rows):
            for j in range(cols):
                if board[i][j] in trie:
                    dfs(i, j, trie[board[i][j]], board[i][j], visited)
        return list(res)