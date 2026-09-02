class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        res = nums[0]
        pos, neg = 1, 1
        for i in range(len(nums)):
            if nums[i] < 0:
                pos, neg = max(nums[i], neg * nums[i]), min(nums[i], pos * nums[i])
            else:
                pos = max(nums[i], pos * nums[i])
                neg = min(nums[i], neg * nums[i])
            if pos > res:
                res = pos
        return res