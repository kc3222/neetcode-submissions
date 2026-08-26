# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def helper(node1, node2, mem):
            if not node1 and not node2:
                if mem:
                    return ListNode(val = 1)
                else:
                    return None
            if not node1:
                if mem == 1:
                    node = ListNode(val = (node2.val + 1) % 10)
                    node.next = helper(None, node2.next, (node2.val + 1) // 10)
                    return node
                else:
                    return node2
            if not node2:
                if mem == 1:
                    node = ListNode(val = (node1.val + 1) % 10)
                    node.next = helper(node1.next, None, (node1.val + 1) // 10)
                    return node
                else:
                    return node1
            node = ListNode(val = (node1.val + node2.val + mem) % 10)
            node.next = helper(node1.next, node2.next, (node1.val + node2.val + mem) // 10)
            return node
        return helper(l1, l2, 0)