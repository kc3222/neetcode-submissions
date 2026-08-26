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
        lst = {}
        lst[head] = Node(x = head.val)
        # First loop
        prev = head
        curr = head.next
        while curr:
            node = Node(x = curr.val)
            lst[curr] = node
            lst[prev].next = node
            prev = curr
            curr = curr.next
        # Second loop
        curr = head
        newCurr = lst[head]
        while curr:
            if curr.random:
                newCurr.random = lst[curr.random]
            curr = curr.next
            newCurr = newCurr.next
        return lst[head]