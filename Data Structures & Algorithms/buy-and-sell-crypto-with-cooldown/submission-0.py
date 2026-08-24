class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if  len(prices) < 2:
            return 0
        # buy: max(sell[i - 2] - prices[i], buy[i - 1]) # We either sell it 2 days ago and buy again or keep holding
        # sell: max(buy[i - 1] + prices[i], sell[i - 1]) # We either buy it 1 day ago and sell now or keep holding
        buy = [0 for i in prices]
        sell = [0 for i in prices]
        buy[0] = -prices[0]
        buy[1] = max(-prices[1], -prices[0])
        sell[1] = max(buy[0] + prices[1], 0)
        for i in range(2, len(prices)):
            buy[i] = max(sell[i - 2] - prices[i], buy[i - 1])
            sell[i] = max(buy[i - 1] + prices[i], sell[i - 1])
        return sell[-1]