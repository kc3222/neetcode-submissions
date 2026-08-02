# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        dct = {}
        curr = head
        while curr:
            dct[curr.next] = curr
            curr = curr.next
        # Reverse
        newHead = ListNode(next = dct[None])
        curr = newHead.next
        while curr in dct:
            nxt = dct[curr]
            curr.next = nxt
            curr = nxt
        curr.next = None
        return newHead.next