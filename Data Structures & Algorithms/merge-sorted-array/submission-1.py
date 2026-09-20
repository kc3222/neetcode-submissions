class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[n: ] = nums1[: m]
        # Swap
        i, j, curr = n, 0, 0
        while i < m + n and j < n:
            if nums1[i] < nums2[j]:
                nums1[curr] = nums1[i]
                i += 1
            else:
                nums1[curr] = nums2[j]
                j += 1
            curr += 1
        if j < n:
            nums1[curr: ] = nums2[j: ]
        