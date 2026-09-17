class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Prefix sum with memoization
        # Memoization reduces the second loop scan while holding O(n) memory
        prefixSum = [0 for i in range(len(nums) + 1)]
        for i in range(len(nums)):
            prefixSum[i + 1] = prefixSum[i] + nums[i]
        # prefix[a...b] = prefix[b + 1] - prefix[a]
        memo = defaultdict(int)
        memo[0] = 1
        res = 0
        for i in range(len(nums)):
            res += memo[prefixSum[i + 1] - k]
            memo[prefixSum[i + 1]] += 1
        return res