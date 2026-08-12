class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backTrack(start, current):
            res.append(current[:])
            for i in range(start, len(nums)):
                current.append(nums[i])
                backTrack(i + 1, current)
                current.pop()
        
        backTrack(0, [])
        return res
        