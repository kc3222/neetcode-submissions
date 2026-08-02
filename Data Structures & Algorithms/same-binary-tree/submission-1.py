# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # BFS
        if not p:
            if not q:
                return True
            else:
                return False
        if not q:
            if p:
                return False
        
        p_stack = [p]
        q_stack = [q]
        while p_stack and q_stack:
            new_p_stack = []
            new_q_stack = []
            for i in range(len(p_stack)):
                p_node = p_stack[i]
                q_node = q_stack[i]
                if p_node.val != q_node.val:
                    return False
                if p_node.left:
                    if q_node.left:
                        new_p_stack.append(p_node.left)
                        new_q_stack.append(q_node.left)
                    else:
                        return False
                if p_node.right:
                    if q_node.right:
                        new_p_stack.append(p_node.right)
                        new_q_stack.append(q_node.right)
                    else:
                        return False
                if q_node.left:
                    if not p_node.left:
                        return False
                if q_node.right:
                    if not p_node.right:
                        return False
            p_stack = new_p_stack
            q_stack = new_q_stack
        return True