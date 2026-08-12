class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        # Initial cases
        if len(self.minHeap) == 0:
            heapq.heappush(self.minHeap, num)
        elif len(self.maxHeap) == 0:
            prev = heapq.heappop(self.minHeap)
            if prev > num:
                heapq.heappush(self.minHeap, prev)
                heapq.heappush(self.maxHeap, -num)
            else:
                heapq.heappush(self.minHeap, num)
                heapq.heappush(self.maxHeap, -prev)
        else:
            currentMin = heapq.heappop(self.minHeap)
            currentMax = -heapq.heappop(self.maxHeap)
            if num >= currentMin:
                heapq.heappush(self.minHeap, num)
            elif num <= currentMax:
                heapq.heappush(self.maxHeap, -num)
            else:
                heapq.heappush(self.minHeap, num)
            heapq.heappush(self.minHeap, currentMin)
            heapq.heappush(self.maxHeap, -currentMax)
            # Rebalance two heaps
            if len(self.minHeap) == len(self.maxHeap) + 2:
                num = heapq.heappop(self.minHeap)
                heapq.heappush(self.maxHeap, -num)
            if len(self.maxHeap) == len(self.minHeap) + 2:
                num = heapq.heappop(self.maxHeap)
                heapq.heappush(self.minHeap, -num)

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            num1 = heapq.heappop(self.minHeap)
            num2 = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, num1)
            heapq.heappush(self.maxHeap, -num2)
            return (num1 + num2) / 2
        elif len(self.minHeap) > len(self.maxHeap):
            num = heapq.heappop(self.minHeap)
            heapq.heappush(self.minHeap, num)
            return num
        else:
            num = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.maxHeap, -num)
            return num
        