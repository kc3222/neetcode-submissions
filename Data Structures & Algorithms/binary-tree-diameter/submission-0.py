# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1
        # longest left + longest right of any node
        res = 0

        def dfs(node):
            nonlocal res
            if not node:
                return -1
            left = dfs(node.left) + 1
            right = dfs(node.right) + 1
            if left + right > res:
                res = left + right
            return max(left, right)
        
        dfs(root)
        return res