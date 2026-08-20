class Solution:
    def rob(self, nums: List[int]) -> int:
        res = [0 for i in range(len(nums) + 1)]
        res[1] = nums[0]
        for i in range(2, len(nums) + 1):
            res[i] = max(res[i - 1], res[i - 2] + nums[i - 1])
        return res[-1]