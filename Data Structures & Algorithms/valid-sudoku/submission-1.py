class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Row check
        for i in range(9):
            row = board[i][:]
            s = set()
            for n in row:
                if n != "." and n in s:
                    return False
                s.add(n)
        # Column check
        for i in range(9):
            col = [row[i] for row in board]
            s = set()
            for n in col:
                if n != "." and n in s:
                    return False
                s.add(n)
        # Box check
        box = [[0, 0], [0, 3], [0, 6], [3,0], [3,3], [3,6], [6,0], [6,3], [6,6]]
        for x, y in box:
            s = set()
            for dx in [0, 1, 2]:
                for dy in [0, 1, 2]:
                    n = board[x + dx][y + dy] 
                    if n != "." and n in s:
                        return False
                    s.add(board[x + dx][y + dy])
        return True