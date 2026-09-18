class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # Sort the people arr
        # Two pointers
        # Keep the smallest with the largest
        # If they overweight, reduce the largest
        people = sorted(people)
        res = 0
        i, j = 0, len(people) - 1
        while i < j:
            if people[i] + people[j] > limit:
                j -= 1
                res += 1
            else:
                i += 1
                j -= 1
                res += 1
        if i == j:
            res += 1
        return res