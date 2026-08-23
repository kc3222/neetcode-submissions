class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Set with occurences
        dct = defaultdict(int)
        for h in hand:
            dct[h] += 1
        nums = sorted(list(dct.keys()), reverse = True)
        # Check if there is enough for a group starting from the lowest number
        while nums:
            starting = nums.pop()
            if dct[starting] == 0:
                continue
            startingOcc = dct[starting]
            for i in range(1, groupSize):
                if dct[starting + i] < startingOcc:
                    return False
                else:
                    dct[starting + i] -= startingOcc
        return True