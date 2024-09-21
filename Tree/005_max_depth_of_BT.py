from typing import Optional


class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def max_depth(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0

    return 1 + max(max_depth(root.left), max_depth(root.right))
