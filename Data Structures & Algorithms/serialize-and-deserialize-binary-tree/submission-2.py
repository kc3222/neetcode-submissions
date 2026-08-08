# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = ""
        if not root:
            return res
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            if node == "N":
                res.append("N")
                continue
            res.append(str(node.val))
            if node.right:
                stack.append(node.right)
            else:
                stack.append("N")
            if node.left:
                stack.append(node.left)
            else:
                stack.append("N")
        return ','.join(res)

    def helper(self, lst):
        val = lst.pop(0)
        if val == "N":
            return None
        node = TreeNode(val = int(val))
        left = self.helper(lst)
        node.left = left
        right = self.helper(lst)
        node.right = right
        return node
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        tree_list = data.split(",")
        if len(tree_list) == 0 or len(tree_list) == 1:
            return None
        root = self.helper(tree_list)
        return root
