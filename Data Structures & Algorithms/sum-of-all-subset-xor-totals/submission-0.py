class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        res = 0
        def backtrack(curr, idx):
            nonlocal res
            num = 0
            for i in curr:
                num ^= i
            res += num

            for i in range(idx, len(nums)):
                curr.append(nums[i])
                backtrack(curr, i + 1)
                curr.pop()
        
        backtrack([], 0)
        return res
