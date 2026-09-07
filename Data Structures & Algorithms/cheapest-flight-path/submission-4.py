class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dct = defaultdict(dict)
        for flight in flights:
            x, y, p = flight
            dct[x][y] = p
        # BFS Bellman-Ford
        res = [float('inf') for i in range(n)]
        res[src] = 0
        stack = [(src, 0)]
        numStops = 0
        while stack and numStops <= k:
            numStops += 1
            nextStack = []
            # Visit city that can arrive at a lower price
            for city, price in stack:
                for nxtCity in dct[city]:
                    nxtPrice = dct[city][nxtCity] + price
                    if nxtPrice < res[nxtCity]:
                        res[nxtCity] = nxtPrice
                        nextStack.append((nxtCity, nxtPrice))
            stack = nextStack
        return res[dst] if res[dst] != float('inf') else -1