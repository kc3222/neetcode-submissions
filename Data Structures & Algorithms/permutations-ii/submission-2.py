class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []

        def backtrack(curr, arr):
            if len(curr) == len(nums):
                res.append(curr[:])
                return
            for i in range(len(arr)):
                if i > 0 and arr[i] == arr[i - 1]: # Ignore the same number
                    continue
                curr.append(arr[i])
                backtrack(curr, arr[:i] + arr[i + 1:])
                curr.pop()

        backtrack([], nums)
        return res