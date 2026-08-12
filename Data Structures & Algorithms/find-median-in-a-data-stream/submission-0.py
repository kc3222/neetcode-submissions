import bisect

class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        idx = bisect.bisect_right(self.arr, num)
        self.arr = self.arr[: idx] + [num] + self.arr[idx: ]

    def findMedian(self) -> float:
        length = len(self.arr)
        if length % 2 == 0:
            med1 = int(length / 2)
            med2 = med1 - 1
            return (self.arr[med1] + self.arr[med2]) / 2
        else:
            med = int((length - 1) / 2)
            return self.arr[med]