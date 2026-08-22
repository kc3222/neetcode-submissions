class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        middle = (low + high) // 2
        def calcHours(num):
            res = 0
            for p in piles:
                res += (p + num - 1) // num
            return res
        while low < middle:
            hours = calcHours(middle)
            if hours <= h:
                high = middle
            else:
                low = middle
            middle = (low + high) // 2
        if calcHours(low) <= h:
            return low
        return high