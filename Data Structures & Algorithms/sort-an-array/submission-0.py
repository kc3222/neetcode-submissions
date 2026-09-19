class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # base case: 0 or 1 element is already sorted
        if len(nums) <= 1:
            return nums

        # split in half, sort each half recursively
        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        # combine the two sorted halves
        return self.merge(left, right)

    def merge(self, a: List[int], b: List[int]) -> List[int]:
        res = []
        i = j = 0

        # repeatedly take the smaller front element
        while i < len(a) and j < len(b):
            if a[i] <= b[j]:  # <= keeps the sort stable
                res.append(a[i])
                i += 1
            else:
                res.append(b[j])
                j += 1

        # one side is exhausted; the other's leftovers are already sorted
        res.extend(a[i:])
        res.extend(b[j:])
        return res