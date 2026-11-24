class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.data, end=" ")

root = Node("K")
root.left = Node("A")
root.right = Node("T")
root.left.left = Node("E")
root.left.right = Node("O")
root.right.left = Node("N")
root.right.right = Node("T")
root.left.left.left = Node("U")
root.left.left.right = Node("A")

print("Postorder Traversal:")
postorder_traversal(root)