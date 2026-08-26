"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        dct = {}

        def getCreate(node):
            if not node:
                return
            if node in dct:
                return dct[node]
            dct[node] = Node(x = node.val)
            dct[node].next = getCreate(node.next)
            dct[node].random = getCreate(node.random)
            return dct[node]

        getCreate(head)
        return dct[head]