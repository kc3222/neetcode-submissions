class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        mid = (high + low) // 2
        if nums[high] > nums[low]:
            return nums[low]
        while high > low + 2:
            if nums[mid] > nums[low]:
                low = mid
                mid = (high + low) // 2
            else:
                high = mid
                mid = (high + low) // 2
        return min(nums[low], nums[high], nums[mid])