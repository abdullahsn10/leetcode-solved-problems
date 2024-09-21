from typing import Optional


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def search_BST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if root is None or root.val == val:
        return root

    if val < root.val:
        return self.searchBST(root.left, val)

    return self.searchBST(root.right, val)
