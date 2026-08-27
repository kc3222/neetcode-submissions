class Node:
    def __init__(self, key, val, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        # Dictionary: key: node
        self.capacity = capacity
        self.currentCapacity = 0
        self.dct = {} # key: node
        # LinkedList
        self.tail = Node(key = -1, val = 0)
        self.head = Node(key = -2, val = 0, next = self.tail)
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.dct:
            val = self.dct[key].val
            self.deleteNode(key)
            self.addNode(key, val)
            return val
        return -1
    
    def deleteNode(self, key):
        if key not in self.dct:
            return
        node = self.dct[key]
        prevNode = node.prev
        nextNode = node.next
        # Delete LRU node
        prevNode.next = nextNode
        nextNode.prev = prevNode
        del self.dct[node.key]
    
    def addNode(self, key, value):
        node = Node(key = key, val = value, next = self.head.next, prev = self.head)
        prevHead = self.head.next
        prevHead.prev = node
        self.head.next = node
        self.dct[key] = node

    def put(self, key: int, value: int) -> None:
        if key not in self.dct:
            self.currentCapacity += 1
            if self.currentCapacity > self.capacity:
                self.deleteNode(self.tail.prev.key)
                self.currentCapacity -= 1
        self.deleteNode(key)
        self.addNode(key, value)
