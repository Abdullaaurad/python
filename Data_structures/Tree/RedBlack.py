class Node:
    def __init__(self, val, color='RED'):
        self.val = val
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

def createNode(val):
    newNode = Node(val)
    newNode.color = 'RED'
    return newNode

def inOrderPrint(root):
    if root is None:
        return
    inOrderPrint(root.left)
    print(f"{root.val}-{'Red' if root.color == 'RED' else 'Black'}")
    inOrderPrint(root.right)

def PreOrderPrint(root):
    if root is None:
        return
    print(f"{root.val}-{'Red' if root.color == 'RED' else 'Black'}")
    PreOrderPrint(root.left)
    PreOrderPrint(root.right)

def leftRotate(root, x):
    y = x.right
    x.right = y.left
    if y.left is not None:
        y.left.parent = x

    y.parent = x.parent

    if x.parent is None:
        root = y
    elif x == x.parent.left:
        x.parent.left = y
    else:
        x.parent.right = y

    y.left = x
    x.parent = y

    return root

def rightRotate(root, y):
    x = y.left
    y.left = x.right
    if x.right is not None:
        x.right.parent = y

    x.parent = y.parent

    if y.parent is None:
        root = x
    elif y == y.parent.left:
        y.parent.left = x
    else:
        y.parent.right = x

    x.right = y
    y.parent = x

    return root

def insertFixup(root, z):
    while z is not None and z.parent is not None and z.parent.color == 'RED':
        if z.parent == z.parent.parent.left:
            y = z.parent.parent.right
            if y is not None and y.color == 'RED':
                z.parent.color = 'BLACK'
                y.color = 'BLACK'
                z.parent.parent.color = 'RED'
                z = z.parent.parent
            else:
                if z == z.parent.right:
                    z = z.parent
                    root = leftRotate(root, z)
                z.parent.color = 'BLACK'
                z.parent.parent.color = 'RED'
                root = rightRotate(root, z.parent.parent)
        else:
            y = z.parent.parent.left
            if y is not None and y.color == 'RED':
                z.parent.color = 'BLACK'
                y.color = 'BLACK'
                z.parent.parent.color = 'RED'
                z = z.parent.parent
            else:
                if z == z.parent.left:
                    z = z.parent
                    root = rightRotate(root, z)
                z.parent.color = 'BLACK'
                z.parent.parent.color = 'RED'
                root = leftRotate(root, z.parent.parent)

    root.color = 'BLACK'
    return root

def insertNode(root, val):
    z = createNode(val)
    if root is None:
        root = z
    else:
        x = root
        y = None

        while x is not None:
            y = x
            if z.val < x.val:
                x = x.left
            elif z.val > x.val:
                x = x.right
            else:
                return root

        z.parent = y
        if z.val < y.val:
            y.left = z
        else:
            y.right = z

    return insertFixup(root, z)

def minValueNode(node):
    current = node
    while current and current.left is not None:
        current = current.left
    return current

def deleteFixup(root, x):
    while x != root and x.color == 'BLACK':
        if x == x.parent.left:
            w = x.parent.right
            if w.color == 'RED':
                w.color = 'BLACK'
                x.parent.color = 'RED'
                root = leftRotate(root, x.parent)
                w = x.parent.right
            if w.left.color == 'BLACK' and w.right.color == 'BLACK':
                w.color = 'RED'
                x = x.parent
            else:
                if w.right.color == 'BLACK':
                    w.left.color = 'BLACK'
                    w.color = 'RED'
                    root = rightRotate(root, w)
                    w = x.parent.right
                w.color = x.parent.color
                x.parent.color = 'BLACK'
                w.right.color = 'BLACK'
                root = leftRotate(root, x.parent)
                x = root
        else:
            w = x.parent.left
            if w.color == 'RED':
                w.color = 'BLACK'
                x.parent.color = 'RED'
                root = rightRotate(root, x.parent)
                w = x.parent.left
            if w.right.color == 'BLACK' and w.left.color == 'BLACK':
                w.color = 'RED'
                x = x.parent
            else:
                if w.left.color == 'BLACK':
                    w.right.color = 'BLACK'
                    w.color = 'RED'
                    root = leftRotate(root, w)
                    w = x.parent.left
                w.color = x.parent.color
                x.parent.color = 'BLACK'
                w.left.color = 'BLACK'
                root = rightRotate(root, x.parent)
                x = root

    x.color = 'BLACK'
    return root

def deleteNode(root, key):
    if root is None:
        return root

    if key < root.val:
        root.left = deleteNode(root.left, key)
    elif key > root.val:
        root.right = deleteNode(root.right, key)
    else:
        if root.left is None or root.right is None:
            temp = root.left if root.left else root.right
            if temp is None:
                temp = root
                root = None
            else:
                root = temp
            del temp
        else:
            temp = minValueNode(root.right)
            root.val = temp.val
            root.right = deleteNode(root.right, temp.val)

    if root is None:
        return root

    if root.color == 'BLACK':
        x = root.left if root.left is not None else root.right
        root = deleteFixup(root, x)

    return root

# Example usage
root = None

n = int(input("How many elements in the Red-Black tree: "))
for _ in range(n):
    value = int(input(f"Enter the value of node {_ + 1}: "))
    root = insertNode(root, value)

print("\nInOrder Traversal:")
inOrderPrint(root)
print("\nPreOrder Traversal:")
PreOrderPrint(root)

m = int(input("How many elements to remove: "))
for _ in range(m):
    value = int(input(f"Enter the value of node {_ + 1}: "))
    root = deleteNode(root, value)

print("\nInOrder Traversal after deletion:")
inOrderPrint(root)
print("\nPreOrder Traversal after deletion:")
PreOrderPrint(root)
