class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dct = set(nums)
        res = 0
        for i in range(len(nums)):
            if nums[i] + 1 in dct:
                continue
            else:
                temp = 0
                while nums[i] - temp in dct:
                    temp += 1
                if temp > res:
                    res = temp
        return res