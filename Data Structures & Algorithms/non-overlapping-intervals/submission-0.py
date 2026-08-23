class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Find most intervals and subtract the difference
        intervals = sorted(intervals, key = lambda x: x[0])
        best = [intervals[0]]
        for i in range(1, len(intervals)):
            interval = intervals[i]
            prevInterval = best[-1]
            if prevInterval[0] <= interval[0] < prevInterval[1]: # Overlapping
                best.pop()
                best.append([interval[0], min(prevInterval[1], interval[1])])
            else:
                best.append(interval)
        return len(intervals) - len(best)