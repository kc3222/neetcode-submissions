class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dp(i, current):
            if i == len(nums):
                if target == current:
                    return 1
                return 0

            if (i, current) in memo:
                return memo[(i, current)]
            add = dp(i + 1, current + nums[i])
            sub = dp(i + 1, current - nums[i])
            memo[(i, current)] = add + sub
            return memo[(i, current)]
            
        res = dp(0, 0)
        return res