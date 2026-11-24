class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.data, end=" ")
        inorder_traversal(root.right)

root = Node("K")
root.left = Node("A")
root.right = Node("T")
root.left.left = Node("E")
root.left.right = Node("O")
root.right.left = Node("N")
root.right.right = Node("T")
root.left.left.left = Node("U")
root.left.left.right = Node("A")

print("Inorder Traversal:")
inorder_traversal(root)