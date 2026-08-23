class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return intervals
        intervals = sorted(intervals, key = lambda x: x[0])
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            prevInterval = res[-1]
            interval = intervals[i]
            if prevInterval[0] <= interval[0] <= prevInterval[1]:
                res.pop()
                res.append([min(prevInterval[0], interval[0]), max(prevInterval[1], interval[1])])
            else:
                res.append(interval)
        return res