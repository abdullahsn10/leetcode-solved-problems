from typing import Optional


class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root is None:
        return root
    root.left, root.right = root.right, root.left
    invert_tree(root.left)
    invert_tree(root.right)
    return root
