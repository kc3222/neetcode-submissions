class Solution:
    def canJump(self, nums: List[int]) -> bool:
        currMaxJump = nums[0]
        currJump = 0
        while currJump < currMaxJump and currMaxJump < len(nums) - 1:
            currJump += 1
            nums[currJump] += currJump
            if nums[currJump] > currMaxJump:
                currMaxJump = nums[currJump]
        return True if currMaxJump >= len(nums) - 1 else False