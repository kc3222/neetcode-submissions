class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set()

        def backtrack(curr, arr):
            if len(curr) == len(nums):
                res.add(tuple(curr))  # tuple is hashable; the set dedupes, so the `in` check isn't needed
                return                # arr is empty here anyway, but return explicitly
            for i in range(len(arr)):
                curr.append(arr[i])
                backtrack(curr, arr[:i] + arr[i + 1:])
                curr.pop()

        backtrack([], nums)
        return [list(t) for t in res]  # convert tuples back to lists