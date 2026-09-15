class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = [0 for i in range(len(prices))] # buy[i] = buy on day i
        sell = [0 for i in range(len(prices))] # sell[i] = sell on day i
        buy[0] = - prices[0]
        for i in range(1, len(prices)):
            # DP
            sell[i] = max(sell[i - 1], buy[i - 1] + prices[i]) # Max of sell yesterday or buy yesterday sell today
            buy[i] = max(buy[i - 1], sell[i - 1] - prices[i]) # Already bought or sell yesterday and buy today
        return max(buy[-1], sell[-1])