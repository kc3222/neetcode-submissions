# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(x, y):
            if x == 0:
                return y
            if y % x == 0:
                return x
            return gcd(abs(x - y), min(x, y))
        if not head:
            return
        if not head.next:
            return head
        self.insertGreatestCommonDivisors(head.next)
        val1 = head.val
        val2 = head.next.val
        gcdVal = gcd(val1, val2)
        node = ListNode(gcdVal, head.next)
        head.next = node
        return head