class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        # Edge cases
        if nums[high] < target:
            return high + 1
        if nums[low] > target:
            return 0
        mid = (low + high) // 2
        while low < mid:
            if nums[mid] == target:
                return mid
            else:
                if nums[mid] > target:
                    high = mid
                    mid = (low + high) // 2
                else:
                    low = mid
                    mid = (low + high) // 2
        if nums[low] == target:
            return low
        return high