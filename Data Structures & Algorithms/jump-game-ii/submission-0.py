class Solution:
    def jump(self, nums: List[int]) -> int:
        length = len(nums)
        res = [float('inf') for _ in nums]
        res[-1] = 0
        for i in range(len(nums) - 2, -1, -1):
            res[i] = min(res[i: min(i + nums[i] + 1, length)]) + 1
        return res[0]