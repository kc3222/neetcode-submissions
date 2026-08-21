"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Heap
        if len(intervals) == 0:
            return 0
        intervals = sorted(intervals, key = lambda x: x.start)
        res = 0
        heap = [intervals[0].end] # Hold all intervals end
        for i in range(1, len(intervals)):
            interval = intervals[i]
            heap_interval_end = heapq.heappop(heap)
            if interval.start < heap_interval_end:
                heapq.heappush(heap, heap_interval_end)
                heapq.heappush(heap, interval.end) # Add a new interval because no existing interval can hold this meeting
            else:
                heapq.heappush(heap, interval.end) # Add it to the earliest meeting
        return len(heap)