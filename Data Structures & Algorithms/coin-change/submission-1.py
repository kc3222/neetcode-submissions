class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        res = [float('inf') for i in range(amount + 1)]
        res[-1] = 0
        for i in range(len(res) - 1, -1, -1):
            if res[i] == float('inf'):
                continue
            for coin in coins:
                if i - coin < 0:
                    continue
                res[i - coin] = min(res[i - coin], res[i] + 1)
        return res[0] if res[0] != float('inf') else -1