class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct = defaultdict(int)
        min_heap = []
        for num in nums:
            dct[num] += 1
        for num in dct:
            if len(min_heap) == k:
                smallest_occ = heapq.heappop(min_heap)
                if dct[num] > smallest_occ[0]:
                    heapq.heappush(min_heap, (dct[num], num))
                else:
                    heapq.heappush(min_heap, smallest_occ)
            else:
                heapq.heappush(min_heap, (dct[num], num))
        res = []
        for val in min_heap:
            res.append(val[1])
        return res