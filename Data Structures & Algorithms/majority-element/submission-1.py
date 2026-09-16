class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer-Moore Algorithm
        candidate = nums[0]
        candidateCount = 1
        for i in range(1, len(nums)):
            if candidateCount == 0:
                candidate = nums[i]
            if nums[i] == candidate:
                candidateCount += 1
            else:
                candidateCount -= 1
        realCount = 0
        for i in range(len(nums)):
            if nums[i] == candidate:
                realCount += 1
        return candidate if realCount >= len(nums) / 2 else 0