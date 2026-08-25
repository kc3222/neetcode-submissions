class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        target = len(nums)
        
        def backTrack(curr):
            if len(curr) == target:
                res.append(curr[:])
            for i in range(len(nums)):
                num = nums.pop(0)
                curr.append(num)
                backTrack(curr)
                curr.pop()
                nums.append(num)
        
        backTrack([])
        return res