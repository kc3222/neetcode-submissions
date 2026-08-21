class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        middle = (high + low) // 2
        while low < middle:
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                high = middle
                middle = (high + low) // 2
            else:
                low = middle
                middle = (high + low) // 2
        if nums[low] == target:
            return low
        if nums[high] == target:
            return high
        return -1