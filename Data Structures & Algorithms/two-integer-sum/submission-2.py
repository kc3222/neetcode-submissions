class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}
        for i in range(len(nums)):
            if nums[i] not in dct:
                dct[nums[i]] = []
            dct[nums[i]].append(i)
        for i in range(len(nums)):
            if target - nums[i] in dct:
                if target - nums[i] != nums[i]:
                    return [i, dct[target - nums[i]][0]]
                else:
                    if len(dct[nums[i]]) > 1:
                        return [dct[nums[i]][0], dct[nums[i]][1]]
        return [0, 0]