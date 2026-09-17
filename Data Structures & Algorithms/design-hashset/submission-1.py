class MyHashSet:

    def __init__(self):
        self.bucketSize = 1000
        self.table = [[] for i in range(self.bucketSize)]

    def add(self, key: int) -> None:
        idx = key % self.bucketSize
        for i in self.table[idx]:
            if i == key:
                return
        self.table[idx].append(key)

    def remove(self, key: int) -> None:
        idx = key % self.bucketSize
        for i in range(len(self.table[idx])):
            if self.table[idx][i] == key:
                self.table[idx].pop(i)
                return

    def contains(self, key: int) -> bool:
        idx = key % self.bucketSize
        for i in self.table[idx]:
            if i == key:
                return True
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)