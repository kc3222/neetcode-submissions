class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        changes = [0, 0]
        for bill in bills:
            if bill == 5:
                changes[0] += 1
            elif bill == 10:
                if changes[0] == 0:
                    return False
                changes[0] -= 1
                changes[1] += 1
            else:
                # 5 10 or 5 5 5
                if changes[1] >= 1 and changes[0] >= 1:
                    changes[1] -= 1
                    changes[0] -= 1
                elif changes[0] >= 3:
                    changes[0] -= 3
                else:
                    return False
        return True