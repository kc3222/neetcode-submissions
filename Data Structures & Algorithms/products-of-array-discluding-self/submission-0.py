class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProd = [1 for num in nums]
        rightProd = [1 for num in nums]
        for i in range(1, len(nums)):
            leftProd[i] = leftProd[i - 1] * nums[i - 1]
        for i in range(len(nums) - 2, -1, -1):
            rightProd[i] = rightProd[i + 1] * nums[i + 1]
        
        res = [1 for _ in nums]
        for i in range(1, len(nums) - 1):
            res[i] = leftProd[i] * rightProd[i]
        res[0] = rightProd[0]
        res[-1] = leftProd[-1]
        return res
