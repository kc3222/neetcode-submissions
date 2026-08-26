# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # DFS
        if not root:
            return 0

        res = 0

        def dfs(curr, maxVal):
            nonlocal res
            if not curr:
                return
            if curr.val >= maxVal:
                res += 1
            dfs(curr.left, max(curr.val, maxVal))
            dfs(curr.right, max(curr.val, maxVal))
        
        dfs(root, root.val)
        return res