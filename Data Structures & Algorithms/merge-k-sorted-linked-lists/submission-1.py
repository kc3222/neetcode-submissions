# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeSortedListNode(self, list1, list2):
        head = ListNode()
        curr = head
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                curr = curr.next
                list1 = list1.next
            else:
                curr.next = list2
                curr = curr.next
                list2 = list2.next
        if list1:
            curr.next = list1
        if list2:
            curr.next = list2
        return head.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode(val = -float('inf'))
        curr = head
        for i in range(len(lists)):
            curr = self.mergeSortedListNode(curr, lists[i])
        return head.next