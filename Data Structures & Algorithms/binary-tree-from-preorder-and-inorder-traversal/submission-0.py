# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # we know that preorder has root at first element and last node at last element
        # inorder has first node at first element and last node at last element
        # we find root from preorder, cut inorder to left and right of root, traverse downward to left and right of root
        if len(preorder) == 0:
            return None
        root_val = preorder[0]
        root = TreeNode(val = root_val)
        for i in range(len(inorder)):
            if inorder[i] == root_val:
                inorder_left = inorder[:i]
                inorder_right = inorder[i + 1:]
                preorder_left = preorder[1: 1 + len(inorder_left)]
                preorder_right = preorder[1 + len(inorder_left) :]
                left_node = self.buildTree(preorder_left, inorder_left)
                right_node = self.buildTree(preorder_right, inorder_right)
                root.left = left_node
                root.right = right_node
        return root
