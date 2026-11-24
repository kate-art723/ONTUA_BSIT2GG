class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preorder_traversal(root):
    if root:
        print(root.data, end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)

root = Node("K")
root.left = Node("A")
root.right = Node("T")
root.left.left = Node("E")
root.left.right = Node("O")
root.right.left = Node("N")
root.right.right = Node("T")
root.left.left.left = Node("U")
root.left.left.right = Node("A")

print("Preorder Traversal:")
preorder_traversal(root)