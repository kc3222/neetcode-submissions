class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = [[]]

        def dfs(i, curr):
            if i == len(nums):
                return 

            curr.append(nums[i])
            res.append(curr[:])
            dfs(i + 1, curr)
            curr.pop()

            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            
            dfs(i + 1, curr)
        
        dfs(0, [])
        return res