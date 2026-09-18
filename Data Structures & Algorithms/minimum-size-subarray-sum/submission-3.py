from bisect import bisect_left
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        # prefix[i] = sum(nums[:i]); prefix[0] = 0, strictly increasing since nums are positive
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        res = n + 1
        for i in range(n):
            # want smallest j > i with prefix[j] - prefix[i] >= target
            # i.e. prefix[j] >= target + prefix[i] -> binary search since prefix is sorted
            needed = target + prefix[i]
            j = bisect_left(prefix, needed, i + 1)
            if j <= n:
                res = min(res, j - i)

        return res if res <= n else 0