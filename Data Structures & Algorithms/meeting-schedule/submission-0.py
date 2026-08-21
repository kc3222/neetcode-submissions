"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = sorted(intervals, key = lambda x: x.start)
        for i in range(1, len(intervals)):
            interval = intervals[i]
            prev_interval = intervals[i - 1]
            if interval.start < prev_interval.end:
                return False
        return True