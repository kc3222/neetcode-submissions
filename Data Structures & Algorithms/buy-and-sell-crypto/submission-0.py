class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy = prices[0]
        for i in range(1, len(prices)):
            res = max(res, prices[i] - buy)
            buy = min(buy, prices[i])
        return res
