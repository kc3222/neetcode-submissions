class StockSpanner:

    def __init__(self):
        self.prices = []

    def next(self, price: int) -> int:
        self.prices.append(price)
        i = len(self.prices) - 1
        res = 0
        while i >= 0:
            if self.prices[i] <= price:
                res += 1
                i -= 1
            else:
                break
        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)