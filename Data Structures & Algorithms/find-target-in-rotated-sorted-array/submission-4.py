class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        mid = (high + low) // 2
        if nums[low] == target:
            return low
        if nums[high] == target:
            return high
        while low < mid:
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                if nums[low] > target and nums[low] < nums[mid]:
                    low = mid
                else:
                    high = mid
            else:
                if nums[high] < target and nums[high] > nums[mid]:
                    high = mid
                else:
                    low = mid
            mid = (low + high) // 2

        if nums[low] == target:
            return low
        if nums[high] == target:
            return high
        return -1