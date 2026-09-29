class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        tempHead = ListNode(0, head)
        parentDict = {}

        # walk exactly `right` steps, recording parents; end is where curr lands
        curr = tempHead
        for idx in range(1, right + 1):
            parentDict[curr.next] = curr
            curr = curr.next
            if idx == left:
                start = curr
        end = curr

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

        # one swap per pair from the outside in; left == right gives 0 swaps
        for _ in range((right - left + 1) // 2):
            nextStart, nextEnd = start.next, parentDict[end]   # grab before swap rewires
            swap(start, end)
            start, end = nextStart, nextEnd

        return tempHead.next