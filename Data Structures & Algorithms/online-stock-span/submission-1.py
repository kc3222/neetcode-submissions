class StockSpanner:

    def __init__(self):
        # Monotonic Stack
        self.prices = [] # (price, numberOfLowerPrices)

    def next(self, price: int) -> int:
        res = 1
        while self.prices:
            prevPrice, numPrices = self.prices.pop()
            if prevPrice <= price:
                res += numPrices
            else:
                self.prices.append([prevPrice, numPrices])
                break
        self.prices.append([price, res])
        return res

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)