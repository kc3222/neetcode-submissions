# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSameTree(self, root1, root2):
        if not root1 and not root2:
            return True
        if root1 and root2 and root1.val == root2.val:
            return self.isSameTree(root1.left, root2.left) and self.isSameTree(root1.right, root2.right)
        return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = [root]
        while stack:
            new_stack = []
            for node in stack:
                if node.val == subRoot.val:
                    if self.isSameTree(node, subRoot):
                        return True
                if node.left:
                    new_stack.append(node.left)
                if node.right:
                    new_stack.append(node.right)
            stack = new_stack
        return False
