# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # BFS
        if not root:
            return root
        stack = [root]
        while stack:
            new_stack = []
            for node in stack:
                node_left = node.left
                node_right = node.right
                node.left = node_right
                node.right = node_left
                if node.left:
                    new_stack.append(node.left)
                if node.right:
                    new_stack.append(node.right)
            stack = new_stack
        return root