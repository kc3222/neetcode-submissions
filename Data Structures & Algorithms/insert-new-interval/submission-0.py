class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval) # Add the new interval
                return res + intervals[i:] # Add the rest
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else: # Update the new interval but not append yet
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1]),
                ]
        res.append(newInterval)
        return res