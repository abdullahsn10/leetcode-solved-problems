from typing import Optional


class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def is_symmetric(self, root: Optional[TreeNode]) -> bool:
    def dfs(left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val != right.val:
            return False
        return dfs(left.left, right.right) and dfs(left.right, right.left)

    return dfs(root.left, root.right)
