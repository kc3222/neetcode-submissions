class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Boyer Moore Algorithm Variation
        candidate1, candidate2, count1, count2 = 0, 1, 0, 0
        for i in range(len(nums)):
            # Check number
            if candidate1 == nums[i]:
                count1 += 1
            elif candidate2 == nums[i]:
                count2 += 1
            else:
                # Check count == 0
                if count1 == 0:
                    candidate1 = nums[i]
                    count1 += 1
                elif count2 == 0:
                    candidate2 = nums[i]
                    count2 += 1
                else: # Reduce both count
                    count1 -= 1
                    count2 -= 1
        realCount1 = 0
        realCount2 = 0
        res = []
        for i in range(len(nums)):
            if nums[i] == candidate1:
                realCount1 += 1
            elif nums[i] == candidate2:
                realCount2 += 1
        if realCount1 > len(nums) / 3:
            res.append(candidate1)
        if realCount2 > len(nums) / 3:
            res.append(candidate2)
        return res