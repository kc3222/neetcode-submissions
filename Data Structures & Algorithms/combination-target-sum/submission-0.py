class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        current = []
        def backTrack(idx, current_sum):
            if current_sum == target:
                res.append(current[:])
            if current_sum > target:
                return
            for i in range(idx, len(nums)):
                current.append(nums[i])
                current_sum += nums[i]
                backTrack(i, current_sum)
                current.pop()
                current_sum -= nums[i]
            return
        backTrack(0, 0)
        return res