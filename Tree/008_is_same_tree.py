from typing import Optional


class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    def same(one, two):
        if one is None and two is None:
            return True
        if one is None or two is None:
            return False
        if one.val != two.val:
            return False
        return same(one.left, two.left) and same(one.right, two.right)

    return same(p, q)
