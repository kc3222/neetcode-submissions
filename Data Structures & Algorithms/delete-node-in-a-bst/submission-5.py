class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val == key:
            # 0 child
            if not root.left and not root.right:
                return None
            # 1 child
            elif root.left and not root.right:
                return root.left
            elif root.right and not root.left:
                return root.right
            # 2 child
            else:
                prev = root
                curr = root.right
                while curr.left:              # leftmost of right subtree = successor
                    prev = curr
                    curr = curr.left
                root.val = curr.val           # copy successor up
                if prev is root:              # successor was root.right itself
                    root.right = curr.right
                else:                         # successor reached by going left
                    prev.left = curr.right    # curr has no left child, splice in its right
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root