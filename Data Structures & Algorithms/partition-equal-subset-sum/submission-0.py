class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sumNums = sum(nums)
        if sumNums % 2 == 1:
            return False
        subsetSum = sumNums / 2

        def backtrack(curr, currSum, i):
            if currSum == subsetSum:
                return True
            elif currSum > subsetSum:
                return False
            
            for j in range(i, len(nums)):
                curr.append(nums[j])
                currSum += nums[j]
                res = backtrack(curr, currSum, j + 1)
                if res:
                    return True
                curr.pop()
                currSum -= nums[j]
            return False
        
        return backtrack([], 0, 0)