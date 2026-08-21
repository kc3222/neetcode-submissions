class MinStack:

    def __init__(self):
        self.stack = []
        self.minHist = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minHist) == 0:
            self.minHist.append(val)
        else:
            self.minHist.append(min(self.minHist[-1], val))

    def pop(self) -> None:
        self.minHist.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minHist[-1]
