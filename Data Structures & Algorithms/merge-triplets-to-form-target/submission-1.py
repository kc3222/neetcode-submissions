class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        targetDct = defaultdict(list)
        for i, t in enumerate(triplets):
            if t[0] == target[0] and t[1] <= target[1] and t[2] <= target[2]:
                targetDct[0].append(i)
            if t[1] == target[1] and t[0] <= target[0] and t[2] <= target[2]:
                targetDct[1].append(i)
            if t[2] == target[2] and t[1] <= target[1] and t[0] <= target[0]:
                targetDct[2].append(i)
        # Greedy
        for i in range(3):
            if len(targetDct[i]) == 0:
                return False
        return True