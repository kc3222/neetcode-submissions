class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = nums[0]
        i = 0
        currSum = 0
        while i < len(nums):
            currSum += nums[i]
            if currSum > res:
                    res = currSum
            if currSum < 0:
                i += 1
                currSum = 0
            else:
                i += 1
        return res