class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Two pointers
        if sum(nums) < target:
            return 0
        i = 0
        curr = 0
        res = len(nums)
        for j in range(len(nums)):
            curr += nums[j]
            while curr >= target and i <= j:
                res = min(res, j - i + 1)
                curr -= nums[i]
                i += 1
        while curr >= target and i < len(nums):
            res = min(res, j - i + 1)
            curr -= nums[i]
            i += 1
        return res