# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sameRoot(self, root, p):
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val == p.val:
                return True
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        if self.lowestCommonAncestor(root.left, p, q):
            return self.lowestCommonAncestor(root.left, p, q)  
        if self.lowestCommonAncestor(root.right, p, q):
            return self.lowestCommonAncestor(root.right, p, q)
        # Root is the common ancestor
        if self.sameRoot(root, p) and self.sameRoot(root, q):
            return root
        return None