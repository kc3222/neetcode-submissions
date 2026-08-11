class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dct = defaultdict(int)
        for task in tasks:
            dct[task] += 1
        heap = []
        for task in dct:
            heapq.heappush(heap, (-dct[task], task))
        cooldown_queue = []
        res = 0
        current_time = 0
        while len(heap) > 0 or len(cooldown_queue) > 0:
            res += 1
            if len(cooldown_queue) > 0:
                if current_time == cooldown_queue[0][1]: # Time to add the task back
                    task, _, prio = cooldown_queue.pop(0)
                    heapq.heappush(heap, (prio, task))
            if len(heap) > 0:
                prio, task = heapq.heappop(heap)
                if prio < -1:
                    cooldown_queue.append([task, current_time + n + 1, prio + 1])
            current_time += 1 # Increase time
        return res