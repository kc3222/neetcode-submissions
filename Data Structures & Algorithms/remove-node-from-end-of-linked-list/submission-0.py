# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        listLength = 0
        newHead = ListNode(next = head)
        curr = head
        while curr:
            listLength += 1
            curr = curr.next
        curr = newHead
        currIdx = -1
        while currIdx != listLength - n - 1:
            curr = curr.next
            currIdx += 1
        currNextNext = curr.next.next
        curr.next = currNextNext
        return newHead.next