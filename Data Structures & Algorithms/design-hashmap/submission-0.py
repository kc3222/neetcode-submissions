class MyHashMap:

    def __init__(self):
        self.bucketSize = 10000
        self.table = [[] for i in range(self.bucketSize)]

    def put(self, key: int, value: int) -> None:
        bucket = self.table[key % self.bucketSize]  # hash key to its bucket
        for pair in bucket:
            if pair[0] == key:  # key already exists -> overwrite value
                pair[1] = value
                return
        bucket.append([key, value])  # new key -> append to the chain

    def get(self, key: int) -> int:
        bucket = self.table[key % self.bucketSize]
        for k, v in bucket:
            if k == key:
                return v
        return -1  # key not in map

    def remove(self, key: int) -> None:
        bucket = self.table[key % self.bucketSize]
        for i, pair in enumerate(bucket):
            if pair[0] == key:
                bucket.pop(i)  # safe to mutate mid-loop since we return right after
                return