class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # dictionary
        # select each number then treat the rest of array as twoSum
        dct = defaultdict(int)
        for num in nums:
            if num == 0:
                dct[num] += 1
            else:
                if dct[num] < 2:
                    dct[num] += 1
        # two sum problem
        res = []
        nums = list(set(nums))
        for i in range(len(nums)):
            dct[nums[i]] -= 1
            temp_dct = dct.copy()
            for j in range(i, len(nums)):
                if temp_dct[nums[j]] == 0:
                    continue
                temp_dct[nums[j]] -= 1
                last_num = - nums[i] - nums[j]
                if temp_dct[last_num] > 0:
                    res.append([nums[i], nums[j], last_num])
                temp_dct[nums[j]] = 0
            dct[nums[i]] = 0
        return res