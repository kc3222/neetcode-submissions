class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 0:
            return 0
        if len(cost) <= 2:
            return min(cost)
        res = [i for i in cost]
        for i in range(2, len(cost)):
            res[i] += min(res[i - 1], res[i - 2])
        return min(res[-1], res[-2])