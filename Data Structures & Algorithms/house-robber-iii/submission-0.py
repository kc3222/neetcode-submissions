# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # DFS
        def dfs(node):
            if not node:
                return 0, 0
            # robbing node and not robbing children vs not robbing node and robbing children
            leftIn, leftOut = dfs(node.left)
            rightIn, rightOut = dfs(node.right)
            return node.val + leftOut + rightOut, max(leftIn, leftOut) + max(rightIn, rightOut)
        
        rootIn, rootOut = dfs(root)
        return max(rootIn, rootOut)
