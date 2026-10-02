class Solution:
    def candy(self, ratings: List[int]) -> int:
        # Two passes
        # Max(fwPass, bwPass)
        fwPass = [1 for i in ratings]
        bwPass = [1 for i in ratings]
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                fwPass[i] = fwPass[i - 1] + 1
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                bwPass[i] = bwPass[i + 1] + 1
        res = 0
        for i in range(len(ratings)):
            res += max(fwPass[i], bwPass[i])
        return res