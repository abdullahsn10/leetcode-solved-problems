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


def max_depth_BFS(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0

    queue = []
    queue.append(root)
    levels = 0
    while queue:
        for _ in range(len(queue)):
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        levels += 1
    return levels
