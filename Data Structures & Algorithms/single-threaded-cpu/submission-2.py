class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [[tasks[i][0], tasks[i][1], i] for i in range(len(tasks))]
        tasks = sorted(tasks)
        heap = []
        order = []
        endTime = 0
        # Loop through, start if available, push to next heap queue
        for task in tasks:
            # Can process previous task
            while task[0] > endTime and heap: # Process all tasks until task can be pushed to heap
                duration, idx, startTime = heapq.heappop(heap)
                endTime = max(endTime, startTime) + duration
                order.append(idx)
            heapq.heappush(heap, (task[1], task[2], task[0]))

        # Process the rest
        while heap:
            duration, idx, startTime = heapq.heappop(heap)
            order.append(idx)
        return order