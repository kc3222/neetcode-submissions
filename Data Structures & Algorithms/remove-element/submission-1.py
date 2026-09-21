class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        i = len(nums) - 1
        j = 0
        while j < i:
            if nums[j] == val:
                nums[j] = nums[i]
                nums[i] = val
                i -= 1
            else:
                j += 1
        return j + 1 if nums[j] != val else j