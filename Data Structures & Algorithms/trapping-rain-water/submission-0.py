class Solution:
    def trap(self, height: List[int]) -> int:
        # Two passes: forward, backward
        # The formula for the trapped water at index i is given by: min(height[l], height[r]) - height[i].
        fwPass = [h for h in height]
        bwPass = [h for h in height]
        for i in range(1, len(fwPass)):
            fwPass[i] = max(fwPass[i - 1], height[i - 1])
        for i in range(len(bwPass) - 2, -1, -1):
            bwPass[i] = max(bwPass[i + 1], height[i + 1])
        # Calculate trapped water at each bar
        res = 0
        for i in range(1, len(height) - 1):
            res += max(min(fwPass[i], bwPass[i]) - height[i], 0)
        return res