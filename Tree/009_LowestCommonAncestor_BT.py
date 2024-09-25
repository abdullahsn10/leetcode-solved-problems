class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if root is None or root == p or root == q:
        return root

    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    # if both left and right not None, then this means
    # the nodes exists in different subtrees so the root
    # is the LCA
    if left and right:
        return root

    # if one side is not none, then either p or q found
    # in that side or the LCA in that side, return it
    return left if left else right
