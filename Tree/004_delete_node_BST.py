from typing import Optional


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def find_min(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root is None:
        return root
    if root.left:
        return find_min(root.left)
    return root


def delete_node(root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    if root is None:
        return root
    if key < root.val:
        root.left = delete_node(root.left, key)
    elif key > root.val:
        root.right = delete_node(root.right, key)
    else:
        # if node has 0 or 1 child
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left

        # if node has 2 childreen
        min_node = find_min(root.right)
        root.val = min_node.val
        root.right = delete_node(root.right, min_node.val)
    return root
