class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dct = defaultdict(int)
        for i in range(min(k + 1, len(nums))):
            dct[nums[i]] += 1
            if dct[nums[i]] == 2:
                return True
        print(dct)
        for i in range(k + 1, len(nums)):
            dct[nums[i - k - 1]] -= 1
            dct[nums[i]] += 1
            if dct[nums[i]] == 2:
                return True
        return False