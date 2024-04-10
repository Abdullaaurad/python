class Node:
    def __init__(self, data, parent=None, color="red"):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None
        self.color = color  # New nodes are always red by default in a red-black tree

def in_order_traversal(node):
    if node:
        in_order_traversal(node.left)
        print(f"{node.data}({node.color})", end=" ")
        in_order_traversal(node.right)

# Example usage:
root = Node(10)
root.left = Node(5, parent=root)
root.right = Node(15, parent=root)

in_order_traversal(root)