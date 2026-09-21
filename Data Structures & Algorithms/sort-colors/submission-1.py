class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = [0, 0, 0]
        for num in nums:
            colors[num] += 1
        r, w, b = 0, colors[0], colors[0] + colors[1]
        i = 0
        while i < colors[0] + colors[1]:
            color = nums[i]
            if color == 1 and i < colors[0]:
                nums[i] = nums[w]
                nums[w] = color
                w += 1
            elif color == 2:
                nums[i] = nums[b]
                nums[b] = color
                b += 1
            else:
                i += 1
        