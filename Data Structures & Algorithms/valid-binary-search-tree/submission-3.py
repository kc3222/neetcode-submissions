# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, root, low, high):
        if not root:
            return True
        if root.left and (root.left.val >= root.val or root.left.val <= low or root.left.val >= high):
            return False
        if root.right and (root.right.val <= root.val or root.right.val <= low or root.right.val >= high):
            return False
        return self.helper(root.left, low, min(high, root.val)) and self.helper(root.right, max(low, root.val), high)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        low, high = float('-inf'), float('inf')
        return self.helper(root, low, high)
