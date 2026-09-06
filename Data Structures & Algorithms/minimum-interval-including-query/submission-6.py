import bisect

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # Sort intervals
        intervals = sorted(intervals, key = lambda x: (x[0], x[1]))
        res = []
        i = 0
        queriesIdx = [i for i in range(len(queries))]
        queries, queriesIdx = map(list, zip(*sorted(zip(queries, queriesIdx))))
        heap = []
        for query in queries:
            # Search for all intervals that starts before the query
            while i < len(intervals) and intervals[i][0] <= query:
                heapq.heappush(heap, (intervals[i][1] - intervals[i][0] + 1, intervals[i][1]))
                i += 1
            # Find the smallest interval
            bestDuration = -1
            while heap:
                duration, endInterval = heapq.heappop(heap)
                if endInterval >= query:
                    bestDuration = duration
                    heapq.heappush(heap, (duration, endInterval))
                    break
            res.append(bestDuration)
        queriesIdx, res = map(list, zip(*sorted(zip(queriesIdx, res))))
        return res