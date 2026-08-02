class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dct = set()
        for i in range(len(nums)):
            if nums[i] in dct:
                return True
            dct.add(nums[i])
        return False