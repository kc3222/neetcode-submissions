class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dct = {}
        
        def backTrack(i, current):
            if (i, current) in dct:
                return dct[(i, current)]
            if current == amount:
                return 1
            elif current > amount:
                return 0
            res = 0
            for c in range(i, len(coins)):
                current += coins[c]
                res += backTrack(c, current)
                current -= coins[c]
            dct[(i, current)] = res
            return dct[(i, current)]
        
        return backTrack(0, 0)