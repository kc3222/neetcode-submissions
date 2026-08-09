import bisect

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        nums = sorted(nums)
        self.nums = nums[max(0, len(nums) - k): len(nums)]
        print(self.nums)
        self.k = k

    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            idx = bisect.bisect_right(self.nums, val)
            self.nums = self.nums[:idx] + [val] + self.nums[idx:]
            return self.nums[0]

        if val < self.nums[0]:
            return self.nums[0]
        else:
            idx = bisect.bisect_right(self.nums, val)
            self.nums = self.nums[1: idx] + [val] + self.nums[idx:]
            return self.nums[0]