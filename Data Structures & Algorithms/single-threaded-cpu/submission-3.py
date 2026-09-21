class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # Attach original index, sort by (enqueueTime, processingTime, index)
        tasks = sorted([enq, proc, i] for i, (enq, proc) in enumerate(tasks))
        heap = []  # (processingTime, index, enqueueTime)
        order = []
        endTime = 0

        for task in tasks:
            # CPU frees up before this task arrives: run queued tasks first
            while heap and task[0] > endTime:
                duration, idx, startTime = heapq.heappop(heap)
                # max() covers the case where the CPU sat idle until startTime
                endTime = max(endTime, startTime) + duration
                order.append(idx)
            heapq.heappush(heap, (task[1], task[2], task[0]))

        # No more arrivals: drain the heap in priority order
        while heap:
            order.append(heapq.heappop(heap)[1])
        return order