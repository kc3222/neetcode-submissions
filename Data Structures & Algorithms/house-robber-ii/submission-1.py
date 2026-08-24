class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        nums1 = [num for num in nums]
        nums1[0] = 0 # Not rob first house
        nums2 = [num for num in nums]
        nums2[-1] = 0 # Not rob last house
        nums2[1] = max(nums2[0], nums2[1])
        # DP
        for i in range(2, len(nums)):
            nums1[i] = max(nums1[i - 2] + nums1[i], nums1[i - 1])
            nums2[i] = max(nums2[i - 2] + nums2[i], nums2[i - 1])
        return max(nums1[-1], nums2[-1])