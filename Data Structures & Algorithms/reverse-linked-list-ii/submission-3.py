# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Build a dict
        # Find the start and end
        # Swap then continue
        if left == right:
            return head
        tempHead = ListNode(0, head)
        parentDict = {}
        curr = tempHead
        start, end = None, None
        idx = 0
        while curr.next:
            if idx == left:
                start = curr
            if idx == right:
                end = curr
            parentDict[curr.next] = curr
            curr = curr.next
            idx += 1
        if idx == right:
            end = curr
        # Edge case
        if start == None or end == None:
            return head
        # Swap
        def swap(x, y):
            yNext = y.next
            yParent = parentDict[y]
            xParent = parentDict[x]
            yParent.next = x
            xParent.next = y
            y.next = x.next
            x.next = yNext

            # the only nodes whose .next changed; fix parent of whatever they now point to
            for node in (xParent, yParent, x, y):
                if node.next:   # tail's next is None
                    parentDict[node.next] = node

        while start != end and start.next != end:
            nextStart = start.next
            nextEnd = parentDict[end]
            swap(start, end)
            start = nextStart
            end = nextEnd
        if start.next == end:
            swap(start, end)
        return tempHead.next