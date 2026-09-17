class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        middle = (low + high) // 2

        def calcDays(k):
            res = 0
            curr = 0
            for i in range(len(weights)):
                if curr + weights[i] > k:
                    res += 1
                    curr = 0
                curr += weights[i]
            res += 1
            return res

        while low < middle:
            tempDays = calcDays(middle)
            if tempDays > days:
                low = middle
            else:
                high = middle
            middle = (low + high) // 2
        if calcDays(low) <= days:
            return low
        return high