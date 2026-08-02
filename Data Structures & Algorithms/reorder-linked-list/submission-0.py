# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Build a dictionary of parent
        # Keep track of tail
        # After each node from head, swap tail node to next
        parentDct = {}
        tail = head
        while tail.next:
            parentDct[tail.next] = tail
            tail = tail.next
        # After each node from head, swap tail
        curr = head
        while curr != tail and curr.next != tail:
            tailPrev = parentDct[tail]
            currNext = curr.next
            curr.next = tail
            tail.next = currNext
            tailPrev.next = None
            curr = currNext
            tail = tailPrev
        return
