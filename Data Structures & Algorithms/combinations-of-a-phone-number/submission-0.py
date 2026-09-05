class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dct = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        res = []
        length = len(digits)
        if length == 0:
            return []

        def backTrack(i, curr):
            if i == length:
                res.append(''.join(curr))
                return

            for j in dct[digits[i]]:
                curr.append(j)
                backTrack(i + 1, curr)
                curr.pop()
            return
        
        backTrack(0, [])
        return res