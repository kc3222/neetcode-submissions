import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}

        def dp(i, j):
            # i: last index
            # j: current index
            # dp: how many more can we add
            if (i, j) in memo:
                return memo[(i, j)]
            if j == len(nums):
                return 0
            res = dp(i, j + 1)  # skip nums[j]
            if i == -1 or nums[j] > nums[i]:
                res = max(res, 1 + dp(j, j + 1))
            memo[(i, j)] = res
            return memo[(i, j)]
        
        return dp(-1, 0)