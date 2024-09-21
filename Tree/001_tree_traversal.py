class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def pre_order_traversal(root):
    # root - left - right
    if root is not None:
        print(root.val, end=" --> ")  # visit root
        pre_order_traversal(root.left)
        pre_order_traversal(root.right)


def in_order_traversal(root):
    # left - root - right
    if root is not None:
        in_order_traversal(root.left)
        print(root.val, end=" --> ")  # visit root
        in_order_traversal(root.right)


def post_order_traversal(root):
    # left - right - root
    if root is not None:
        post_order_traversal(root.left)
        post_order_traversal(root.right)
        print(root.val, end=" --> ")  # visit root


def level_order_traversal(root):
    if root is None:
        return

    queue = []
    queue.append(root)

    while queue:
        node = queue.pop(0)
        print(node.val, end=" --> ")  # visit node
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


def level_order_list(root: TreeNode) -> list:
    if root is None:
        return []
    queue = []
    levels = []
    queue.append(root)
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.pop(0)
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        levels.append(level)
    return levels


# create a tree
root = TreeNode(60)

root.left = TreeNode(20)
root.right = TreeNode(70)

root.left.left = TreeNode(10)
root.left.right = TreeNode(40)

root.left.right.left = TreeNode(30)
root.left.right.right = TreeNode(50)


# traversing alg
print("In Order Traversal: ")
in_order_traversal(root)
print()

print("Pre Order Traversal: ")
pre_order_traversal(root)
print()

print("Post Order Traversal: ")
post_order_traversal(root)
print()

print("Level Order Traversal (BFS): ")
level_order_traversal(root)
print()

print(level_order_list(root))
